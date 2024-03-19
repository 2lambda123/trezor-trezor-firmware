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

#ifndef TREZORHAL_XDISPLAY_H
#define TREZORHAL_XDISPLAY_H

// This is a universal API for controlling different types of display controllers.
//
// Currently, following displays displays are supported
//
// VG-2864KSWEG01  - OLED Mono / 128x64 pixels  / SPI
//                 - Model T1B1 / Model T2B1
//
// UG-2828SWIG01   - OLED Mono / 128x128 pixels / Parallel
//                 - Early revisions of T2B1
//
// ST7789V         - TFT RGB   / 240x240 pixels / Parallel
//                 - Model T2T1 / Model T3T1
//
// ILI9341         - TFT RGB   / 320x240 pixels / Parallel / LTDC + SPI
//                 - STM32F429I-DISC1 Discovery Board
//
// MIPI            -
//                 - STM32U5A9J-DK Discovery Board


// Fully initializes the display controller.
void xdisplay_init(void);

// Called in application to reinitialize an already initialized display controller
// without any distrubing visible effect (blinking, etc.).
void xdisplay_soft_init(void);

// Waits for any backround operations (such as DMA copying)
// and returns.
//
// The function provides a barrier when jumping between
// boardloader/bootloader and firmware.
void xdisplay_dma_barrier(void);


// Sets display backlight level ranging from 0 (off)..255 (maximum).
//
// The default backligt level is 0. Without settings it
// to some higher value the displayed pixels are not visible.
// Beware that his also applies to the emulator.
//
// Returns the set level (usually the same value or the
// closest value to the `level` argument)
int xdisplay_set_backlight(int level);

// Gets current display level ranging from 0 (off)..255 (maximum).
int xdisplay_get_backlight(void);

// Sets the display orientation.
//
// May accept one of following values: 0, 90, 180, 270
// but accepted values are model-dependent.
// Default display orientation is always 0.
//
// Returns the set orientation
int xdisplay_set_orientation(int angle);

// Gets the display's current orientation
//
// Returned value is one of 0, 90, 180, 270.
int xdisplay_get_orientation(void);


#if defined(FRAMEBUFFER)
// Provides pointer to the inactive (writeable) framebuffer.
//
// If framebuffer is not available yet due to display refreshing etc.,
// the function may block until the buffer is ready to write.
void * xdisplay_acquire_fb(void);
#endif

#if defined(FRAMEBUFFER)
// Swaps the frame buffers
//
// The function wait for vertical synchronization and
// swaps the active (currently displayed) and the inactive frame buffers.
void xdisplay_swap_fb(void);
#endif

#if ! defined(FRAMEBUFFER)
// Waits for the vertical synchronization pulse.
//
// Used for synchronization with display refresh cycle
// to achieve tearless UX if possible when not using a frame buffer.
void xdisplay_wait_for_sync(void);
#endif

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


// Save the screen content to a file.
//
// The function is available onwly on the emulator
#if defined(TREZOR_EMULATOR)
void xdisplay_save_to_file(const char *prefix);
#endif


#endif  // TREZORHAL_XDISPLAY_H