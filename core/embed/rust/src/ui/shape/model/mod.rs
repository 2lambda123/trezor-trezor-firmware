#[cfg(feature = "model_tr")]
pub mod model_tr;
#[cfg(feature = "model_tr")]
pub use model_tr::render_on_display;

#[cfg(feature = "model_tt")]
pub mod model_tt;
#[cfg(feature = "model_tt")]
pub use model_tt::render_on_display;

#[cfg(feature = "model_t3t1")]
pub mod model_t3t1;
#[cfg(feature = "model_t3t1")]
pub use model_t3t1::render_on_display;

