use crate::ui::{
    display::Color,
    geometry::{Offset, Point, Rect},
};

use super::{BasicCanvas, Bitmap, BitmapFormat, BitmapView, Canvas, Viewport};

#[cfg(feature = "ui_blurring")]
use crate::ui::shape::DrawingCache;

/// A struct representing 16-bit (RGB565) color canvas
pub struct Rgb565Canvas<'a> {
    bitmap: Bitmap<'a>,
    viewport: Viewport,
}

impl<'a> Rgb565Canvas<'a> {
    /// Creates a new canvas with the specified size and buffer.
    ///
    /// Optionally minimal height can be specified and then the height
    /// of the new bitmap is adjusted to the buffer size.
    ///
    /// Returns None if the buffer is not big enough.
    pub fn new(size: Offset, min_height: Option<i16>, buff: &'a mut [u8]) -> Option<Self> {
        let bitmap = Bitmap::new_mut(BitmapFormat::RGB565, None, size, min_height, buff)?;
        let viewport = Viewport::from_size(bitmap.size());
        Some(Self { bitmap, viewport })
    }

    /// Returns the specified row as a mutable slice.
    ///
    /// Returns None if row is out of range.
    pub fn row_mut(&mut self, row: i16) -> Option<&mut [u16]> {
        self.bitmap.row_mut(row)
    }
}

impl<'a> BasicCanvas for Rgb565Canvas<'a> {
    fn size(&self) -> Offset {
        self.bitmap.size()
    }

    fn viewport(&self) -> Viewport {
        self.viewport
    }

    fn set_viewport(&mut self, viewport: Viewport) {
        self.viewport = viewport.absolute_clip(self.bounds());
    }

    fn fill_rect(&mut self, r: Rect, color: Color, alpha: u8) {
        let r = r.translate(self.viewport.origin);
        self.bitmap.rgb565_fill(r, self.viewport.clip, color, alpha);
    }

    fn draw_bitmap(&mut self, r: Rect, bitmap: BitmapView) {
        let r = r.translate(self.viewport.origin);
        self.bitmap.rgb565_copy(r, self.viewport.clip, &bitmap);
    }
}

impl<'a> Canvas for Rgb565Canvas<'a> {
    fn view(&self) -> BitmapView {
        BitmapView::new(&self.bitmap)
    }

    fn draw_pixel(&mut self, pt: Point, color: Color) {
        let pt = pt + self.viewport.origin;
        if self.viewport.clip.contains(pt) {
            if let Some(row) = self.row_mut(pt.y) {
                row[pt.x as usize] = color.into();
            }
        }
    }

    fn blend_pixel(&mut self, pt: Point, color: Color, alpha: u8) {
        let pt = pt + self.viewport.origin;
        if self.viewport.clip.contains(pt) {
            if let Some(row) = self.row_mut(pt.y) {
                let pixel = &mut row[pt.x as usize];
                let bg_color: Color = (*pixel).into();
                *pixel = bg_color.blend(color, alpha).into();
            }
        }
    }

    fn blend_bitmap(&mut self, r: Rect, src: BitmapView) {
        let r = r.translate(self.viewport.origin);
        self.bitmap.rgb565_blend(r, self.viewport.clip, &src);
    }

    #[cfg(feature = "ui_blurring")]
    fn blur_rect(&mut self, r: Rect, radius: usize, cache: &DrawingCache) {
        let clip = r
            .translate(self.viewport.origin)
            .intersect(self.viewport.clip);

        let ofs = radius as i16;

        if clip.width() > 2 * ofs - 1 && clip.height() > 2 * ofs - 1 {
            let mut blur_cache = cache.blur();
            let (blur, _) = unwrap!(
                blur_cache.get(clip.size(), radius, None),
                "Too small blur buffer"
            );

            loop {
                if let Some(y) = blur.push_ready() {
                    let row = unwrap!(self.row_mut(y + clip.y0)); // can't panic
                    blur.push(&row[clip.x0 as usize..clip.x1 as usize]);
                }
                if let Some(y) = blur.pop_ready() {
                    let row = unwrap!(self.row_mut(y + clip.y0)); // can't panic
                    blur.pop(&mut row[clip.x0 as usize..clip.x1 as usize], None);
                    if y + 1 >= clip.height() {
                        break;
                    }
                }
            }
        }
    }
}
