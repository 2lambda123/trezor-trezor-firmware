/*
 * This file is part of the Trezor project, https://trezor.io/
 *
 * Copyright (c) SatoshiLabs
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdbool.h>
#include <stdint.h>
#include TREZOR_BOARD
#include STM32_HAL_H

#include "xdisplay.h"

#ifdef USE_CONSUMPTION_MASK
#include "consumption_mask.h"
#endif

#define OLED_SETCONTRAST 0x81
#define OLED_DISPLAYALLON_RESUME 0xA4
#define OLED_DISPLAYALLON 0xA5
#define OLED_NORMALDISPLAY 0xA6
#define OLED_INVERTDISPLAY 0xA7
#define OLED_DISPLAYOFF 0xAE
#define OLED_DISPLAYON 0xAF
#define OLED_SETDISPLAYOFFSET 0xD3
#define OLED_SETCOMPINS 0xDA
#define OLED_SETVCOMDETECT 0xDB
#define OLED_SETDISPLAYCLOCKDIV 0xD5
#define OLED_SETPRECHARGE 0xD9
#define OLED_SETMULTIPLEX 0xA8
#define OLED_SETLOWCOLUMN 0x00
#define OLED_SETHIGHCOLUMN 0x10
#define OLED_SETSTARTLINE 0x40
#define OLED_MEMORYMODE 0x20
#define OLED_COMSCANINC 0xC0
#define OLED_COMSCANDEC 0xC8
#define OLED_SEGREMAP 0xA0
#define OLED_CHARGEPUMP 0x8D

  // Display controller initialization sequence
static const uint8_t vg_2864ksweg01_init_seq[] = {
    OLED_DISPLAYOFF,
    OLED_SETDISPLAYCLOCKDIV,
    0x80,
    OLED_SETMULTIPLEX,
    0x3F,  // 128x64
    OLED_SETDISPLAYOFFSET,
    0x00,
    OLED_SETSTARTLINE | 0x00,
    OLED_CHARGEPUMP,
    0x14,
    OLED_MEMORYMODE,
    0x00,
    OLED_SEGREMAP | 0x01,
    OLED_COMSCANDEC,
    OLED_SETCOMPINS,
    0x12,  // 128x64
    OLED_SETCONTRAST,
    0xCF,
    OLED_SETPRECHARGE,
    0xF1,
    OLED_SETVCOMDETECT,
    0x40,
    OLED_DISPLAYALLON_RESUME,
    OLED_NORMALDISPLAY,
    OLED_DISPLAYON
  };

// Display driver context.
typedef struct {
  // SPI driver instance
  SPI_HandleTypeDef spi;
  // Frame buffer (8-bit Mono)
  uint8_t framebuf[DISPLAY_RESX * DISPLAY_RESY];
  // Current display orientation (0 or 180)
  int orientation_angle;
  // Current backlight level ranging from 0 to 255
  int backlight_level;
} display_t;


// Display driver instance
static display_t g_display;


// Configures SPI driver/controller
static bool display_spi_init(display_t * display) {
  display->spi.Instance = OLED_SPI;
  display->spi.State = HAL_SPI_STATE_RESET;
  display->spi.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_16;
  display->spi.Init.Direction = SPI_DIRECTION_2LINES;
  display->spi.Init.CLKPhase = SPI_PHASE_1EDGE;
  display->spi.Init.CLKPolarity = SPI_POLARITY_LOW;
  display->spi.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  display->spi.Init.CRCPolynomial = 7;
  display->spi.Init.DataSize = SPI_DATASIZE_8BIT;
  display->spi.Init.FirstBit = SPI_FIRSTBIT_MSB;
  display->spi.Init.NSS = SPI_NSS_HARD_OUTPUT;
  display->spi.Init.TIMode = SPI_TIMODE_DISABLE;
  display->spi.Init.Mode = SPI_MODE_MASTER;

  return (HAL_OK == HAL_SPI_Init(&spi_handle)) ? true : false;
}


// Sends specified number of bytes to the display via SPI interface
static void display_send_bytes(display_t * display, const uint8_t *data, size_t len) {
  volatile int32_t timeout = 1000; // !@# why???
  for (int i = 0; i < timeout; i++)
    ;

  if (HAL_OK != HAL_SPI_Transmit(&display->spi, (uint8_t *)data, len, 1000)) {
    // TODO: error
    return;
  }
  while (HAL_SPI_STATE_READY != HAL_SPI_GetState(&display->spi)) {
  }
}

#define ROW_BYTE(src) 0 \
  | (*(src + (0 * DISPLAY_RESX)) ? 128 : 0) \
  | (*(src + (1 * DISPLAY_RESX)) ? 64 : 0) \
  | (*(src + (2 * DISPLAY_RESX)) ? 32 : 0) \
  | (*(src + (3 * DISPLAY_RESX)) ? 16 : 0) \
  | (*(src + (4 * DISPLAY_RESX)) ? 8 : 0) \
  | (*(src + (5 * DISPLAY_RESX)) ? 4 : 0) \
  | (*(src + (6 * DISPLAY_RESX)) ? 2 : 0) \
  | (*(src + (7 * DISPLAY_RESX)) ? 1 : 0);


// Copies the framebuffer to the display via SPI interface
static void display_send_fb(display_t * display) {
  static const uint8_t cursor_set_seq[3] = {
    OLED_SETLOWCOLUMN | 0x00,
    OLED_SETHIGHCOLUMN | 0x00,
    OLED_SETSTARTLINE | 0x00
  };

  // SPI select
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_RESET);
  // Set the cursor to the screen top-left corner
  display_send_bytes(display, &cursor_set_seq[0], sizeof(cursor_set_seq));

  // SPI deselect
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_SET);
  // Set to DATA
  HAL_GPIO_WritePin(OLED_DC_PORT, OLED_DC_PIN, GPIO_PIN_SET);
  // SPI select
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_RESET);

  // Send whole framebuffer to the display
  for (int y = 0; y < DISPLAY_RESY / 8; y++) {
    uint8_t buff[DISPLAY_RESX];
    uint8_t *src = &display->framebuf[y * DISPLAY_RESX * 8];

    if (display->orientation_angle == 0) {
      for (int x = 0; x < DISPLAY_RESX; x++) {
        buff[x] = ROW_BYTE(src);
        src++;
      }
    } else {
      for (int x = DISPLAY_RESX - 1; x >= 0; x--) {
        buff[x] = ROW_BYTE(src);
        src++;
      }
    }

    if (HAL_OK != HAL_SPI_Transmit(&display->spi, &buff[0], sizeof(buff), 1000)) {
      // TODO: error
      return;
    }
  }

  while (HAL_SPI_STATE_READY != HAL_SPI_GetState(&display->spi)) {
  }

  // SPI deselect
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_SET);
  // Set to CMD
  HAL_GPIO_WritePin(OLED_DC_PORT, OLED_DC_PIN, GPIO_PIN_RESET);
}


void xdisplay_init(void) {
  display_t * display = &g_display;

  memset(display, 0, sizeof(display_t));
  display->backlight_level = 255;

  OLED_DC_CLK_ENA();
  OLED_CS_CLK_ENA();
  OLED_RST_CLK_ENA();
  OLED_SPI_SCK_CLK_ENA();
  OLED_SPI_MOSI_CLK_ENA();
  OLED_SPI_CLK_ENA();

  GPIO_InitTypeDef GPIO_InitStructure;

  // Set GPIO for OLED display
  GPIO_InitStructure.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStructure.Pull = GPIO_NOPULL;
  GPIO_InitStructure.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
  GPIO_InitStructure.Alternate = 0;
  GPIO_InitStructure.Pin = OLED_CS_PIN;
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_RESET);
  HAL_GPIO_Init(OLED_CS_PORT, &GPIO_InitStructure);
  GPIO_InitStructure.Pin = OLED_DC_PIN;
  HAL_GPIO_WritePin(OLED_DC_PORT, OLED_DC_PIN, GPIO_PIN_RESET);
  HAL_GPIO_Init(OLED_DC_PORT, &GPIO_InitStructure);
  GPIO_InitStructure.Pin = OLED_RST_PIN;
  HAL_GPIO_WritePin(OLED_RST_PORT, OLED_RST_PIN, GPIO_PIN_RESET);
  HAL_GPIO_Init(OLED_RST_PORT, &GPIO_InitStructure);

  // Enable SPI 1 for OLED display
  GPIO_InitStructure.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStructure.Pull = GPIO_NOPULL;
  GPIO_InitStructure.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
  GPIO_InitStructure.Alternate = OLED_SPI_AF;
  GPIO_InitStructure.Pin = OLED_SPI_SCK_PIN;
  HAL_GPIO_Init(OLED_SPI_SCK_PORT, &GPIO_InitStructure);
  GPIO_InitStructure.Pin = OLED_SPI_MOSI_PIN;
  HAL_GPIO_Init(OLED_SPI_MOSI_PORT, &GPIO_InitStructure);

  // Initialize SPI controller
  display_spi_init(display);

  // Set to CMD
  HAL_GPIO_WritePin(OLED_DC_PORT, OLED_DC_PIN, GPIO_PIN_RESET);
  // SPI deselect
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_SET);

  // Reset the LCD
  HAL_GPIO_WritePin(OLED_RST_PORT, OLED_RST_PIN, GPIO_PIN_SET);
  HAL_Delay(1);
  HAL_GPIO_WritePin(OLED_RST_PORT, OLED_RST_PIN, GPIO_PIN_RESET);
  HAL_Delay(1);
  HAL_GPIO_WritePin(OLED_RST_PORT, OLED_RST_PIN, GPIO_PIN_SET);

  // SPI select
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_RESET);
  // Send initialization command sequence
  display_send_bytes(display, &vg_2864ksweg01_init_seq[0], sizeof(vg_2864ksweg01_init_seq));
  // SPI deselect
  HAL_GPIO_WritePin(OLED_CS_PORT, OLED_CS_PIN, GPIO_PIN_SET);

  display_send_fb(display);
}


void xdisplay_soft_init(void) {
  display_t * display = &g_display;

  memset(display, 0, sizeof(display_t));
  display->backlight_level = 255;

  display_spi_init(display);
}


void xdisplay_dma_barrier(void) {
  // Not implemented
}


int xdisplay_set_backlight(int level) {
  display_t * display = &g_display;

  display->backlight_level = 255;
  return display->backlight_level;
}

int xdisplay_get_backlight(void) {
  display_t * display = &g_display;

  return display->backlight_level;
}

int xdisplay_set_orientation(int angle) {
  display_t * display = &g_display;

  if (angle != display->orientation_angle) {
    if (angle == 0 || angle == 180) {
      display->orientation_angle = angle;
      display_send_fb(display);
    }
  }

  return display->orientation_angle;
}

int xdisplay_get_orientation(void) {
  display_t * display = &g_display;

  return display->orientation_angle;
}


void * xdisplay_acquire_fb(void) {
  display_t * display = &g_display;

  return &display->framebuff[0];
}


void xdisplay_swap_fb(void) {
  display_t * display = &g_display;

#if defined USE_CONSUMPTION_MASK && !defined BOARDLOADER
  // This is an intentional randomization of the consumption masking algorithm
  // after every change on the display
  consumption_mask_randomize();
#endif

  // Sends the current frame buffer to the display
  display_send_fb(display);
}


// Functions for drawing on display
/*

// Fills a rectangle with a specified color
void xdisplay_fill_rect(gdc_dma2d_t *dp);

// Copies an RGB565 bitmap to specified rectangle
void xdisplay_copy_rgb565(gdc_dma2d_t *dp);

// Copies a MONO4 bitmap to specified rectangle
void xdisplay_copy_mono4(gdc_dma2d_t *dp);

// Copies a MONO1P bitmap to specified rectangle
void xdisplay_copy_mono1p(gdc_dma2d_t *dp);
*/

