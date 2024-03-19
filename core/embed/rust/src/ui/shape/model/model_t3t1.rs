use crate::ui::{
    display,
    display::Color,
    geometry::{Offset, Rect},
    shape::{BasicCanvas, DirectRenderer, DrawingCache, Rgb565Canvas, Viewport},
};

use static_alloc::Bump;

pub fn render_on_display<'a, F>(clip: Option<Rect>, bg_color: Option<Color>, func: F)
where
    F: FnOnce(&mut DirectRenderer<'_, 'a, Rgb565Canvas<'a>>),
{
    #[link_section = ".no_dma_buffers"]
    static mut BUMP_A: Bump<[u8; 40 * 1024]> = Bump::uninit();

    #[link_section = ".buf"]
    static mut BUMP_B: Bump<[u8; 16 * 1024]> = Bump::uninit();

    let bump_a = unsafe { &mut *core::ptr::addr_of_mut!(BUMP_A) };
    let bump_b = unsafe { &mut *core::ptr::addr_of_mut!(BUMP_B) };
    {
        bump_a.reset();
        bump_b.reset();

        let fb_addr = crate::trezorhal::display::get_fb_addr().0 as *mut u8;
        let fb = unsafe { core::slice::from_raw_parts_mut(fb_addr, 240 * 240 * 2)};

        let cache = DrawingCache::new(bump_a, bump_b);
        let mut canvas = unwrap!(Rgb565Canvas::new(Offset::new(240, 240), None, fb));

        if let Some(clip) = clip {
            canvas.set_viewport(Viewport::new(clip));
        }

        let mut target = DirectRenderer::new(&mut canvas, bg_color, &cache);

        func(&mut target);

        display::refresh();
    }
}

