#include <stdint.h>

#if TREZOR_FONT_BPP != 4
#error Wrong TREZOR_FONT_BPP (expected 4)
#endif
#define Font_TTSatoshi_Medium_21_HEIGHT 21
#define Font_TTSatoshi_Medium_21_MAX_HEIGHT 21
#define Font_TTSatoshi_Medium_21_BASELINE 4
extern const uint8_t* const Font_TTSatoshi_Medium_21[126 + 1 - 32];
extern const uint8_t Font_TTSatoshi_Medium_21_glyph_nonprintable[];
