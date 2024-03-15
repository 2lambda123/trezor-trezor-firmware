#ifndef _BRG_ENDIAN_H
#define _BRG_ENDIAN_H

#define IS_BIG_ENDIAN      4321 /* byte 0 is most significant (mc68k) */
#define IS_LITTLE_ENDIAN   1234 /* byte 0 is least significant (i386) */

#define PLATFORM_BYTE_ORDER IS_LITTLE_ENDIAN

#endif
