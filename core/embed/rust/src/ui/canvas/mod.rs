pub mod bluralgo;
pub mod display;
pub mod mono;
pub mod mono1;
pub mod mono4;
mod octant;
pub mod rgb;
pub mod rgb565;
pub mod rgba8888;

use crate::ui::geometry::{Offset, Rect};

/// The Viewport concept is foundation for clipping and translating
/// during drawing on the general canvas.
///
/// The Viewport structure comprises a rectangle representing the
/// clipping area and a drawing origin (or offset), which is applied
/// to all coordinates passed to the drawing functions.
///
/// Two coordination systems exist - "absolute" and "relative."
///
/// In the "absolute" coordinate system, (0, 0) is at the left-top of
/// a referenced canvas (device or bitmap).
///
/// Relative coordinates are with respect to the viewport origin.
/// The relative coordinate (0, 0) is located at (viewport.origin.x,
/// viewport.origin.y).
///
/// Conversion between "absolute" and "relative" coordinates is straightforward:
///
/// pt_absolute = pt_relative.translate(viewport.origin)
///
/// pt_relative = pt_absolute.translate(-viewport.origin)
///
/// The Viewport's clipping area and origin are always in "absolute"
/// coordinates. Canvas objects utilize the viewport to translate "relative"
/// coordinates passed to drawing functions into "absolute" coordinates that
/// correspond to the target device or bitmap.

#[derive(Copy, Clone)]
pub struct Viewport {
    /// Clipping rectangle relative to the canvas top-left corner
    pub clip: Rect,
    /// Offset applied to all coordinates before clipping
    pub origin: Offset,
}

impl Viewport {
    // Creates a new viewport with specified size and origin at (0,0)
    pub fn from_size(size: Offset) -> Viewport {
        Self {
            clip: Rect::from_size(size),
            origin: Offset::zero(),
        }
    }

    /// Returns the width of the viewport
    pub fn width(&self) -> i16 {
        // TODO: candidate to remove
        self.clip.width()
    }

    /// Returns the height of the viewport
    pub fn height(&self) -> i16 {
        // TODO: candidate to remove
        self.clip.width()
    }

    /// Checks if the viewport intersects with the specified rectangle
    /// given in relative coordinates.
    pub fn contains(&self, r: Rect) -> bool {
        r.translate(self.origin).has_intersection(self.clip)
    }

    pub fn translate(self, offset: Offset) -> Viewport {
        Self {
            clip: self.clip.translate(offset),
            origin: self.origin + offset,
        }
    }

    // Creates a new viewport with the new origin given in
    // absolute coordinates
    pub fn with_origin(self, origin: Offset) -> Viewport {
        Self { origin, ..self }
    }

    /// Creates a clip of the viewport containing only the specified rectangle
    /// given in absolute coordinates. The origin of the new viewport
    /// remains unchanged.
    pub fn absolute_clip(self, r: Rect) -> Viewport {
        Self {
            clip: r.intersect(self.clip),
            ..self
        }
    }

    /// Creates a clip of the viewport containing only the specified rectangle
    /// given in relative coordinates. The origin of the new viewport
    /// remains unchanged.
    pub fn relative_clip(self, r: Rect) -> Viewport {
        Self {
            clip: r.translate(self.origin).intersect(self.clip),
            ..self
        }
    }

    /// Creates a clip of the viewport containing only the specified rectangle
    /// given in relative coordinates. The origin of the new viewport
    /// is set to the top-left corner of the rectangle.
    pub fn relative_window(&self, r: Rect) -> Viewport {
        let clip = r.translate(self.origin).intersect(self.clip);
        let origin = self.origin + (clip.top_left() - self.clip.top_left());
        Self { clip, origin }
    }
}