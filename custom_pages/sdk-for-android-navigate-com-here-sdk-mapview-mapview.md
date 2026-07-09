---
title: "MapView (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapview"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapView.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">android.view.View
<div className="inheritance">android.view.ViewGroup
<div className="inheritance">android.widget.FrameLayout
<div className="inheritance">com.here.sdk.mapview.MapView</div>
</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>android.graphics.drawable.Drawable.Callback</code>, <code>android.view.accessibility.AccessibilityEventSource</code>, <code>android.view.KeyEvent.Callback</code>, <code>android.view.ViewManager</code>, <code>android.view.ViewParent</code>, <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public class </span><span className="element-name type-name-label">MapView</span>
<span className="extends-implements">extends android.widget.FrameLayout
implements <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></span></div>
<div className="block">A view that can display a map.

 <p>The content of the map is controlled by <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a>,
 which is accessible by calling <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#getMapScene()"><code>getMapScene()</code></a>. To display a map, map scene needs
 to be loaded with <a href="sdk-for-android-navigate-mapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)"><code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)</code></a>.

 Manipulating the way the map is displayed is possible using <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera" title="class in com.here.sdk.mapview"><code>MapCamera</code></a>, which is
 accessible by calling <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#getCamera()"><code>getCamera()</code></a>.

 Gesture handling can be modified through the <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> object, which is
 accessible by calling <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#getGestures()"><code>getGestures()</code></a>.

 
 To use the MapView the following application permissions need to be present:
 android.permission.INTERNET and android.permission.ACCESS_NETWORK_STATE

 
<code>MapView</code> can draw the map using either <code>SurfaceView</code> or <code>TextureView</code>.

 <code>SurfaceView</code> is the default method, offers best performance and works best for single
 screen applications where there's a single <code>MapView</code> which is not part of a complex view
 hierarchy and takes no part in any UI animations. This method is known to cause graphical
 glitches in some scenarios (like embedding multiple <code>MapView</code>s inside a view pager),
 especially on Android 12 and newer.

 <code>TextureView</code> is less performant, but behaves like any other view and can be easily
 transformed and animated, making it a better fit for applications with complex UI and/or
 multiple <code>MapView</code>s as part of a complex view hierarchy.

 Rendering mode can only be set when creating a <code>MapView</code>, by setting
 <a href="sdk-for-android-navigate-mapviewoptions#renderMode"><code>MapViewOptions.renderMode</code></a> and passing the options to the constructor.

 

 When dealing with view coordinates, physical pixels are used. MapView provides ways
 to translate between view and geographic coordinates using
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#viewToGeoCoordinates(com.here.sdk.core.Point2D)"><code>viewToGeoCoordinates(Point2D)</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)"><code>geoToViewCoordinates(GeoCoordinates)</code></a> methods.
 Note that those two methods only work when the MapView is fully ready, so if there is a need
 to call them during lifecycle changes, they should be called from within
 <a href="sdk-for-android-navigate-mapview-onreadylistener#onMapViewReady()"><code>MapView.OnReadyListener.onMapViewReady()</code></a>. See Lifecycle section below for more details.

 
Two caching mechanisms are supported. First is in-memory cache, which keeps some number
 of map tiles around in memory to avoid repeated network requests or storage reads.
 The second mechanism is persistent cache that stores downloaded map data on the device.
 Persistent cache requires storage permission to be granted.

 
For <code>MapView</code> to work correctly, it is required to call its lifecycle
 methods from the owner Activity: <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onResume()"><code>onResume()</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onPause()"><code>onPause()</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onDestroy()"><code>onDestroy()</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onSaveInstanceState(android.os.Bundle)"><code>onSaveInstanceState(Bundle)</code></a>.

 When dealing with multiple <code>MapView</code>s in a single Activity,
 an extra identifier needs to be passed to <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle,java.lang.String)"><code>onCreate(Bundle, String)</code></a> and
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onSaveInstanceState(android.os.Bundle,java.lang.String)"><code>onSaveInstanceState(Bundle, String)</code></a>. This identifier needs to be unique
 to all the <code>MapView</code>s owned by the <code>Activity</code> and needs to be the same
 when recreating the <code>Activity</code>.

 A <code>MapView</code> is considered valid only after
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle,java.lang.String)"><code>onCreate(Bundle, String)</code></a> and before
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onDestroy()"><code>onDestroy()</code></a> is called. <code>MapView</code> is also invalidated when the
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> it is using is destroyed.
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#isValid()"><code>isValid()</code></a> can be used to check the state of <code>MapView</code>.

 <code>MapView</code> offers additional lifecycle event exposed through <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview"><code>MapView.OnReadyListener</code></a>.
 This can be used to determine when <code>MapView</code> is fully ready for action, which means that
 map scene is loaded and drawing surface is ready to render a map. This is important
 for coordinate conversion methods and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#getViewportSize()"><code>getViewportSize()</code></a>, which work only when those
 conditions are met. When <code>OnReadyListener</code> is set in <code>Activity</code>'s <code>onCreate()</code>
 before any other operation is performed on the <code>MapView</code>, then
 <a href="sdk-for-android-navigate-mapview-onreadylistener#onMapViewReady()"><code>MapView.OnReadyListener.onMapViewReady()</code></a> is called:
 <ul>
<li>after map scene is successfully loaded for the first time</li>
<li>some time after <code>Activity</code>'s <code>onResume()</code>, assuming map scene had been
     loaded before</li>
</ul>
Note: Before using any API in this class, <code>SDKNativeEngine</code> must be already initialized.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview">MapView.OnReadyListener</a></code></div>
<div className="col-last even-row-color">
<div className="block">Listener that gets notified when MapView is fully initialized and ready to handle all
 operations, which means that map scene is loaded and drawing surface is ready to render
 a map.</div>
</div>
<div className="col-first odd-row-color"><code>static interface </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-takescreenshotcallback" title="interface in com.here.sdk.mapview">MapView.TakeScreenshotCallback</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Callback to be called on retrieval of screenshot.</div>
</div>
<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-viewpin" title="interface in com.here.sdk.mapview">MapView.ViewPin</a></code></div>
<div className="col-last even-row-color">
<div className="block">A ViewPin is used to display Android views at a fixed location on the map.</div>
</div>
</div>
<div className="inherited-list">

<code>android.widget.FrameLayout.LayoutParams</code></div>
<div className="inherited-list">

<code>android.view.ViewGroup.MarginLayoutParams, android.view.ViewGroup.OnHierarchyChangeListener</code></div>
<div className="inherited-list">

<code>android.view.View.AccessibilityDelegate, android.view.View.BaseSavedState, android.view.View.DragShadowBuilder, android.view.View.MeasureSpec, android.view.View.OnApplyWindowInsetsListener, android.view.View.OnAttachStateChangeListener, android.view.View.OnCapturedPointerListener, android.view.View.OnClickListener, android.view.View.OnContextClickListener, android.view.View.OnCreateContextMenuListener, android.view.View.OnDragListener, android.view.View.OnFocusChangeListener, android.view.View.OnGenericMotionListener, android.view.View.OnHoverListener, android.view.View.OnKeyListener, android.view.View.OnLayoutChangeListener, android.view.View.OnLongClickListener, android.view.View.OnScrollChangeListener, android.view.View.OnSystemUiVisibilityChangeListener, android.view.View.OnTouchListener, android.view.View.OnUnhandledKeyEventListener</code></div>
<div className="inherited-list">

<code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase-mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="inherited-list">
<h3 id="fields-inherited-from-class-android.view.ViewGroup">Fields inherited from class android.view.ViewGroup</h3>
<code>CLIP_TO_PADDING_MASK, FOCUS_AFTER_DESCENDANTS, FOCUS_BEFORE_DESCENDANTS, FOCUS_BLOCK_DESCENDANTS, LAYOUT_MODE_CLIP_BOUNDS, LAYOUT_MODE_OPTICAL_BOUNDS, PERSISTENT_ALL_CACHES, PERSISTENT_ANIMATION_CACHE, PERSISTENT_NO_CACHE, PERSISTENT_SCROLLING_CACHE</code></div>
<div className="inherited-list">
<h3 id="fields-inherited-from-class-android.view.View">Fields inherited from class android.view.View</h3>
<code>ACCESSIBILITY_DATA_SENSITIVE_AUTO, ACCESSIBILITY_DATA_SENSITIVE_NO, ACCESSIBILITY_DATA_SENSITIVE_YES, ACCESSIBILITY_LIVE_REGION_ASSERTIVE, ACCESSIBILITY_LIVE_REGION_NONE, ACCESSIBILITY_LIVE_REGION_POLITE, ALPHA, AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR, AUTOFILL_HINT_CREDIT_CARD_NUMBER, AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE, AUTOFILL_HINT_EMAIL_ADDRESS, AUTOFILL_HINT_NAME, AUTOFILL_HINT_PASSWORD, AUTOFILL_HINT_PHONE, AUTOFILL_HINT_POSTAL_ADDRESS, AUTOFILL_HINT_POSTAL_CODE, AUTOFILL_HINT_USERNAME, AUTOFILL_TYPE_DATE, AUTOFILL_TYPE_LIST, AUTOFILL_TYPE_NONE, AUTOFILL_TYPE_TEXT, AUTOFILL_TYPE_TOGGLE, CONTENT_SENSITIVITY_AUTO, CONTENT_SENSITIVITY_NOT_SENSITIVE, CONTENT_SENSITIVITY_SENSITIVE, DRAG_FLAG_ACCESSIBILITY_ACTION, DRAG_FLAG_GLOBAL, DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION, DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION, DRAG_FLAG_GLOBAL_SAME_APPLICATION, DRAG_FLAG_GLOBAL_URI_READ, DRAG_FLAG_GLOBAL_URI_WRITE, DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START, DRAG_FLAG_OPAQUE, DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG, DRAWING_CACHE_QUALITY_AUTO, DRAWING_CACHE_QUALITY_HIGH, DRAWING_CACHE_QUALITY_LOW, EMPTY_STATE_SET, ENABLED_FOCUSED_SELECTED_STATE_SET, ENABLED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, ENABLED_FOCUSED_STATE_SET, ENABLED_FOCUSED_WINDOW_FOCUSED_STATE_SET, ENABLED_SELECTED_STATE_SET, ENABLED_SELECTED_WINDOW_FOCUSED_STATE_SET, ENABLED_STATE_SET, ENABLED_WINDOW_FOCUSED_STATE_SET, FIND_VIEWS_WITH_CONTENT_DESCRIPTION, FIND_VIEWS_WITH_TEXT, FOCUS_BACKWARD, FOCUS_DOWN, FOCUS_FORWARD, FOCUS_LEFT, FOCUS_RIGHT, FOCUS_UP, FOCUSABLE, FOCUSABLE_AUTO, FOCUSABLES_ALL, FOCUSABLES_TOUCH_MODE, FOCUSED_SELECTED_STATE_SET, FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, FOCUSED_STATE_SET, FOCUSED_WINDOW_FOCUSED_STATE_SET, GONE, HAPTIC_FEEDBACK_ENABLED, IMPORTANT_FOR_ACCESSIBILITY_AUTO, IMPORTANT_FOR_ACCESSIBILITY_NO, IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS, IMPORTANT_FOR_ACCESSIBILITY_YES, IMPORTANT_FOR_AUTOFILL_AUTO, IMPORTANT_FOR_AUTOFILL_NO, IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_AUTOFILL_YES, IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_CONTENT_CAPTURE_AUTO, IMPORTANT_FOR_CONTENT_CAPTURE_NO, IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_CONTENT_CAPTURE_YES, IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS, INVISIBLE, KEEP_SCREEN_ON, LAYER_TYPE_HARDWARE, LAYER_TYPE_NONE, LAYER_TYPE_SOFTWARE, LAYOUT_DIRECTION_INHERIT, LAYOUT_DIRECTION_LOCALE, LAYOUT_DIRECTION_LTR, LAYOUT_DIRECTION_RTL, MEASURED_HEIGHT_STATE_SHIFT, MEASURED_SIZE_MASK, MEASURED_STATE_MASK, MEASURED_STATE_TOO_SMALL, NO_ID, NOT_FOCUSABLE, OVER_SCROLL_ALWAYS, OVER_SCROLL_IF_CONTENT_SCROLLS, OVER_SCROLL_NEVER, PRESSED_ENABLED_FOCUSED_SELECTED_STATE_SET, PRESSED_ENABLED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_FOCUSED_STATE_SET, PRESSED_ENABLED_FOCUSED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_SELECTED_STATE_SET, PRESSED_ENABLED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_STATE_SET, PRESSED_ENABLED_WINDOW_FOCUSED_STATE_SET, PRESSED_FOCUSED_SELECTED_STATE_SET, PRESSED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_FOCUSED_STATE_SET, PRESSED_FOCUSED_WINDOW_FOCUSED_STATE_SET, PRESSED_SELECTED_STATE_SET, PRESSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_STATE_SET, PRESSED_WINDOW_FOCUSED_STATE_SET, REQUESTED_FRAME_RATE_CATEGORY_DEFAULT, REQUESTED_FRAME_RATE_CATEGORY_HIGH, REQUESTED_FRAME_RATE_CATEGORY_LOW, REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE, REQUESTED_FRAME_RATE_CATEGORY_NORMAL, ROTATION, ROTATION_X, ROTATION_Y, SCALE_X, SCALE_Y, SCREEN_STATE_OFF, SCREEN_STATE_ON, SCROLL_AXIS_HORIZONTAL, SCROLL_AXIS_NONE, SCROLL_AXIS_VERTICAL, SCROLL_CAPTURE_HINT_AUTO, SCROLL_CAPTURE_HINT_EXCLUDE, SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS, SCROLL_CAPTURE_HINT_INCLUDE, SCROLL_INDICATOR_BOTTOM, SCROLL_INDICATOR_END, SCROLL_INDICATOR_LEFT, SCROLL_INDICATOR_RIGHT, SCROLL_INDICATOR_START, SCROLL_INDICATOR_TOP, SCROLLBAR_POSITION_DEFAULT, SCROLLBAR_POSITION_LEFT, SCROLLBAR_POSITION_RIGHT, SCROLLBARS_INSIDE_INSET, SCROLLBARS_INSIDE_OVERLAY, SCROLLBARS_OUTSIDE_INSET, SCROLLBARS_OUTSIDE_OVERLAY, SELECTED_STATE_SET, SELECTED_WINDOW_FOCUSED_STATE_SET, SOUND_EFFECTS_ENABLED, STATUS_BAR_HIDDEN, STATUS_BAR_VISIBLE, SYSTEM_UI_FLAG_FULLSCREEN, SYSTEM_UI_FLAG_HIDE_NAVIGATION, SYSTEM_UI_FLAG_IMMERSIVE, SYSTEM_UI_FLAG_IMMERSIVE_STICKY, SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN, SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION, SYSTEM_UI_FLAG_LAYOUT_STABLE, SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR, SYSTEM_UI_FLAG_LIGHT_STATUS_BAR, SYSTEM_UI_FLAG_LOW_PROFILE, SYSTEM_UI_FLAG_VISIBLE, SYSTEM_UI_LAYOUT_FLAGS, TEXT_ALIGNMENT_CENTER, TEXT_ALIGNMENT_GRAVITY, TEXT_ALIGNMENT_INHERIT, TEXT_ALIGNMENT_TEXT_END, TEXT_ALIGNMENT_TEXT_START, TEXT_ALIGNMENT_VIEW_END, TEXT_ALIGNMENT_VIEW_START, TEXT_DIRECTION_ANY_RTL, TEXT_DIRECTION_FIRST_STRONG, TEXT_DIRECTION_FIRST_STRONG_LTR, TEXT_DIRECTION_FIRST_STRONG_RTL, TEXT_DIRECTION_INHERIT, TEXT_DIRECTION_LOCALE, TEXT_DIRECTION_LTR, TEXT_DIRECTION_RTL, TRANSLATION_X, TRANSLATION_Y, TRANSLATION_Z, VIEW_LOG_TAG, VISIBLE, WINDOW_FOCUSED_STATE_SET, X, Y, Z</code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#%3Cinit%3E(android.content.Context)">MapView</a><wbr/>(android.content.Context context)</code></div>
<div className="col-last even-row-color">
<div className="block">Simple constructor to use when creating a map view from code.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#%3Cinit%3E(android.content.Context,android.util.AttributeSet)">MapView</a><wbr/>(android.content.Context context,
 android.util.AttributeSet attrs)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#%3Cinit%3E(android.content.Context,android.util.AttributeSet,int)">MapView</a><wbr/>(android.content.Context context,
 android.util.AttributeSet attrs,
 int defStyleAttr)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#%3Cinit%3E(android.content.Context,com.here.sdk.mapview.MapViewOptions)">MapView</a><wbr/>(android.content.Context context,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options)</code></div>
<div className="col-last odd-row-color">
<div className="block">Simple constructor to use when creating a map view from code.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,android.content.Context,android.util.AttributeSet,int)">MapView</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 android.content.Context context,
 android.util.AttributeSet attrs,
 int defStyleAttr)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapview.MapViewOptions,android.content.Context,android.util.AttributeSet,int)">MapView</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options,
 android.content.Context context,
 android.util.AttributeSet attrs,
 int defStyleAttr)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-android.widget.FrameLayout">Methods inherited from class android.widget.FrameLayout</h3>
<code>checkLayoutParams, generateDefaultLayoutParams, generateLayoutParams, generateLayoutParams, getAccessibilityClassName, getConsiderGoneChildrenWhenMeasuring, getMeasureAllChildren, onLayout, onMeasure, setForegroundGravity, setMeasureAllChildren, shouldDelayChildPressedState</code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-android.view.ViewGroup">Methods inherited from class android.view.ViewGroup</h3>
<code>addChildrenForAccessibility, addExtraDataToAccessibilityNodeInfo, addFocusables, addKeyboardNavigationClusters, addStatesFromChildren, addTouchables, addView, addView, addView, addView, addView, addViewInLayout, addViewInLayout, attachLayoutAnimationParameters, attachViewToParent, bringChildToFront, canAnimate, childDrawableStateChanged, childHasTransientStateChanged, cleanupLayoutState, clearChildFocus, clearDisappearingChildren, clearFocus, debug, detachAllViewsFromParent, detachViewFromParent, detachViewFromParent, detachViewsFromParent, dispatchApplyWindowInsets, dispatchCapturedPointerEvent, dispatchConfigurationChanged, dispatchCreateViewTranslationRequest, dispatchDisplayHint, dispatchDragEvent, dispatchDraw, dispatchDrawableHotspotChanged, dispatchFinishTemporaryDetach, dispatchFreezeSelfOnly, dispatchGenericFocusedEvent, dispatchGenericPointerEvent, dispatchHoverEvent, dispatchKeyEvent, dispatchKeyEventPreIme, dispatchKeyShortcutEvent, dispatchPointerCaptureChanged, dispatchProvideAutofillStructure, dispatchProvideStructure, dispatchRestoreInstanceState, dispatchSaveInstanceState, dispatchScrollCaptureSearch, dispatchSetActivated, dispatchSetPressed, dispatchSetSelected, dispatchStartTemporaryDetach, dispatchSystemUiVisibilityChanged, dispatchThawSelfOnly, dispatchTouchEvent, dispatchTrackballEvent, dispatchUnhandledMove, dispatchVisibilityChanged, dispatchWindowFocusChanged, dispatchWindowInsetsAnimationEnd, dispatchWindowInsetsAnimationPrepare, dispatchWindowInsetsAnimationProgress, dispatchWindowInsetsAnimationStart, dispatchWindowSystemUiVisiblityChanged, dispatchWindowVisibilityChanged, drawableStateChanged, drawChild, endViewTransition, findFocus, findOnBackInvokedDispatcherForChild, findViewsWithText, focusableViewAvailable, focusSearch, gatherTransparentRegion, getChildAt, getChildCount, getChildDrawingOrder, getChildDrawingOrder, getChildMeasureSpec, getChildStaticTransformation, getChildVisibleRect, getClipChildren, getClipToPadding, getDescendantFocusability, getFocusedChild, getLayoutAnimation, getLayoutAnimationListener, getLayoutMode, getLayoutTransition, getNestedScrollAxes, getOverlay, getPersistentDrawingCache, getTouchscreenBlocksFocus, hasFocus, hasTransientState, indexOfChild, invalidateChild, invalidateChildInParent, isAlwaysDrawnWithCacheEnabled, isAnimationCacheEnabled, isChildrenDrawingOrderEnabled, isChildrenDrawnWithCacheEnabled, isLayoutSuppressed, isMotionEventSplittingEnabled, isTransitionGroup, jumpDrawablesToCurrentState, layout, measureChild, measureChildren, measureChildWithMargins, notifySubtreeAccessibilityStateChanged, offsetDescendantRectToMyCoords, offsetRectIntoDescendantCoords, onAttachedToWindow, onCreateDrawableState, onDescendantInvalidated, onDetachedFromWindow, onInterceptHoverEvent, onInterceptTouchEvent, onNestedFling, onNestedPreFling, onNestedPrePerformAccessibilityAction, onNestedPreScroll, onNestedScroll, onNestedScrollAccepted, onRequestFocusInDescendants, onRequestSendAccessibilityEvent, onResolvePointerIcon, onStartNestedScroll, onStopNestedScroll, onViewAdded, onViewRemoved, propagateRequestedFrameRate, recomputeViewAttributes, removeAllViews, removeAllViewsInLayout, removeDetachedView, removeView, removeViewAt, removeViewInLayout, removeViews, removeViewsInLayout, requestChildFocus, requestChildRectangleOnScreen, requestDisallowInterceptTouchEvent, requestFocus, requestSendAccessibilityEvent, requestTransparentRegion, restoreDefaultFocus, scheduleLayoutAnimation, setAddStatesFromChildren, setAlwaysDrawnWithCacheEnabled, setAnimationCacheEnabled, setChildrenDrawingCacheEnabled, setChildrenDrawingOrderEnabled, setChildrenDrawnWithCacheEnabled, setClipChildren, setClipToPadding, setDescendantFocusability, setLayoutAnimation, setLayoutAnimationListener, setLayoutMode, setLayoutTransition, setMotionEventSplittingEnabled, setOnHierarchyChangeListener, setPersistentDrawingCache, setRequestedFrameRate, setStaticTransformationsEnabled, setTouchscreenBlocksFocus, setTransitionGroup, setWindowInsetsAnimationCallback, showContextMenuForChild, showContextMenuForChild, startActionModeForChild, startActionModeForChild, startLayoutAnimation, startViewTransition, suppressLayout, updateViewLayout</code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-android.view.View">Methods inherited from class android.view.View</h3>
<code>addFocusables, addOnAttachStateChangeListener, addOnLayoutChangeListener, addOnUnhandledKeyEventListener, animate, announceForAccessibility, autofill, autofill, awakenScrollBars, awakenScrollBars, awakenScrollBars, bringToFront, buildDrawingCache, buildDrawingCache, buildLayer, callOnClick, cancelDragAndDrop, cancelLongPress, cancelPendingInputEvents, canResolveLayoutDirection, canResolveTextAlignment, canResolveTextDirection, canScrollHorizontally, canScrollVertically, checkInputConnectionProxy, clearAnimation, clearPendingCredentialRequest, clearViewTranslationCallback, combineMeasuredStates, computeHorizontalScrollExtent, computeHorizontalScrollOffset, computeHorizontalScrollRange, computeScroll, computeSystemWindowInsets, computeVerticalScrollExtent, computeVerticalScrollOffset, computeVerticalScrollRange, createAccessibilityNodeInfo, createContextMenu, destroyDrawingCache, dispatchGenericMotionEvent, dispatchNestedFling, dispatchNestedPreFling, dispatchNestedPrePerformAccessibilityAction, dispatchNestedPreScroll, dispatchNestedScroll, dispatchPopulateAccessibilityEvent, draw, drawableHotspotChanged, findOnBackInvokedDispatcher, findViewById, findViewWithTag, fitSystemWindows, focusSearch, forceHasOverlappingRendering, forceLayout, generateDisplayHash, generateViewId, getAccessibilityDelegate, getAccessibilityLiveRegion, getAccessibilityNodeProvider, getAccessibilityPaneTitle, getAccessibilityTraversalAfter, getAccessibilityTraversalBefore, getAllowedHandwritingDelegatePackageName, getAllowedHandwritingDelegatorPackageName, getAlpha, getAnimation, getAnimationMatrix, getApplicationWindowToken, getAttributeResolutionStack, getAttributeSourceResourceMap, getAutofillHints, getAutofillId, getAutofillType, getAutofillValue, getBackground, getBackgroundTintBlendMode, getBackgroundTintList, getBackgroundTintMode, getBaseline, getBottom, getBottomFadingEdgeStrength, getBottomPaddingOffset, getCameraDistance, getClipBounds, getClipBounds, getClipToOutline, getContentCaptureSession, getContentDescription, getContentSensitivity, getContext, getContextMenuInfo, getDefaultFocusHighlightEnabled, getDefaultSize, getDisplay, getDrawableState, getDrawingCache, getDrawingCache, getDrawingCacheBackgroundColor, getDrawingCacheQuality, getDrawingRect, getDrawingTime, getElevation, getExplicitStyle, getFilterTouchesWhenObscured, getFitsSystemWindows, getFocusable, getFocusables, getFocusedRect, getForeground, getForegroundGravity, getForegroundTintBlendMode, getForegroundTintList, getForegroundTintMode, getFrameContentVelocity, getGlobalVisibleRect, getGlobalVisibleRect, getHandler, getHandwritingBoundsOffsetBottom, getHandwritingBoundsOffsetLeft, getHandwritingBoundsOffsetRight, getHandwritingBoundsOffsetTop, getHandwritingDelegateFlags, getHandwritingDelegatorCallback, getHasOverlappingRendering, getHeight, getHitRect, getHorizontalFadingEdgeLength, getHorizontalScrollbarHeight, getHorizontalScrollbarThumbDrawable, getHorizontalScrollbarTrackDrawable, getId, getImportantForAccessibility, getImportantForAutofill, getImportantForContentCapture, getKeepScreenOn, getKeyDispatcherState, getLabelFor, getLayerType, getLayoutDirection, getLayoutParams, getLeft, getLeftFadingEdgeStrength, getLeftPaddingOffset, getLocalVisibleRect, getLocationInSurface, getLocationInWindow, getLocationOnScreen, getMatrix, getMeasuredHeight, getMeasuredHeightAndState, getMeasuredState, getMeasuredWidth, getMeasuredWidthAndState, getMinimumHeight, getMinimumWidth, getNextClusterForwardId, getNextFocusDownId, getNextFocusForwardId, getNextFocusLeftId, getNextFocusRightId, getNextFocusUpId, getOnFocusChangeListener, getOutlineAmbientShadowColor, getOutlineProvider, getOutlineSpotShadowColor, getOverScrollMode, getPaddingBottom, getPaddingEnd, getPaddingLeft, getPaddingRight, getPaddingStart, getPaddingTop, getParent, getParentForAccessibility, getPendingCredentialCallback, getPendingCredentialRequest, getPivotX, getPivotY, getPointerIcon, getPreferKeepClearRects, getReceiveContentMimeTypes, getRequestedFrameRate, getResources, getRevealOnFocusHint, getRight, getRightFadingEdgeStrength, getRightPaddingOffset, getRootSurfaceControl, getRootView, getRootWindowInsets, getRotation, getRotationX, getRotationY, getScaleX, getScaleY, getScrollBarDefaultDelayBeforeFade, getScrollBarFadeDuration, getScrollBarSize, getScrollBarStyle, getScrollCaptureHint, getScrollIndicators, getScrollX, getScrollY, getSolidColor, getSourceLayoutResId, getStateDescription, getStateListAnimator, getSuggestedMinimumHeight, getSuggestedMinimumWidth, getSupplementalDescription, getSystemGestureExclusionRects, getSystemUiVisibility, getTag, getTag, getTextAlignment, getTextDirection, getTooltipText, getTop, getTopFadingEdgeStrength, getTopPaddingOffset, getTouchables, getTouchDelegate, getTransitionAlpha, getTransitionName, getTranslationX, getTranslationY, getTranslationZ, getUniqueDrawingId, getVerticalFadingEdgeLength, getVerticalScrollbarPosition, getVerticalScrollbarThumbDrawable, getVerticalScrollbarTrackDrawable, getVerticalScrollbarWidth, getViewTranslationResponse, getViewTreeObserver, getVisibility, getWidth, getWindowAttachCount, getWindowId, getWindowInsetsController, getWindowSystemUiVisibility, getWindowToken, getWindowVisibility, getWindowVisibleDisplayFrame, getX, getY, getZ, hasExplicitFocusable, hasFocusable, hasNestedScrollingParent, hasOnClickListeners, hasOnLongClickListeners, hasOverlappingRendering, hasPointerCapture, hasWindowFocus, inflate, invalidate, invalidate, invalidate, invalidateDrawable, invalidateOutline, isAccessibilityDataSensitive, isAccessibilityFocused, isAccessibilityHeading, isActivated, isAttachedToWindow, isAutoHandwritingEnabled, isClickable, isContentSensitive, isContextClickable, isCredential, isDirty, isDrawingCacheEnabled, isDuplicateParentStateEnabled, isEnabled, isFocusable, isFocusableInTouchMode, isFocused, isFocusedByDefault, isForceDarkAllowed, isHandwritingDelegate, isHapticFeedbackEnabled, isHardwareAccelerated, isHorizontalFadingEdgeEnabled, isHorizontalScrollBarEnabled, isHovered, isImportantForAccessibility, isImportantForAutofill, isImportantForContentCapture, isInEditMode, isInLayout, isInTouchMode, isKeyboardNavigationCluster, isLaidOut, isLayoutDirectionResolved, isLayoutRequested, isLongClickable, isNestedScrollingEnabled, isOpaque, isPaddingOffsetRequired, isPaddingRelative, isPivotSet, isPreferKeepClear, isPressed, isSaveEnabled, isSaveFromParentEnabled, isScreenReaderFocusable, isScrollbarFadingEnabled, isScrollContainer, isSelected, isShowingLayoutBounds, isShown, isSoundEffectsEnabled, isTemporarilyDetached, isTextAlignmentResolved, isTextDirectionResolved, isVerticalFadingEdgeEnabled, isVerticalScrollBarEnabled, isVisibleToUserForAutofill, keyboardNavigationClusterSearch, measure, mergeDrawableStates, offsetLeftAndRight, offsetTopAndBottom, onAnimationEnd, onAnimationStart, onApplyWindowInsets, onCancelPendingInputEvents, onCapturedPointerEvent, onCheckIsTextEditor, onConfigurationChanged, onCreateContextMenu, onCreateInputConnection, onCreateViewTranslationRequest, onCreateVirtualViewTranslationRequests, onDisplayHint, onDragEvent, onDraw, onDrawForeground, onDrawScrollBars, onFilterTouchEventForSecurity, onFinishInflate, onFinishTemporaryDetach, onFocusChanged, onGenericMotionEvent, onHoverChanged, onHoverEvent, onInitializeAccessibilityEvent, onInitializeAccessibilityNodeInfo, onKeyDown, onKeyLongPress, onKeyMultiple, onKeyPreIme, onKeyShortcut, onKeyUp, onOverScrolled, onPointerCaptureChange, onPopulateAccessibilityEvent, onProvideAutofillStructure, onProvideAutofillVirtualStructure, onProvideContentCaptureStructure, onProvideStructure, onProvideVirtualStructure, onReceiveContent, onRestoreInstanceState, onRtlPropertiesChanged, onSaveInstanceState, onScreenStateChanged, onScrollCaptureSearch, onScrollChanged, onSetAlpha, onSizeChanged, onStartTemporaryDetach, onTrackballEvent, onViewTranslationResponse, onVirtualViewTranslationResponses, onVisibilityAggregated, onVisibilityChanged, onWindowFocusChanged, onWindowSystemUiVisibilityChanged, onWindowVisibilityChanged, overScrollBy, performAccessibilityAction, performClick, performContextClick, performContextClick, performHapticFeedback, performHapticFeedback, performLongClick, performLongClick, performReceiveContent, playSoundEffect, post, postDelayed, postInvalidate, postInvalidate, postInvalidateDelayed, postInvalidateDelayed, postInvalidateOnAnimation, postInvalidateOnAnimation, postOnAnimation, postOnAnimationDelayed, refreshDrawableState, releasePointerCapture, removeCallbacks, removeOnAttachStateChangeListener, removeOnLayoutChangeListener, removeOnUnhandledKeyEventListener, reportAppJankStats, requestApplyInsets, requestFitSystemWindows, requestFocus, requestFocus, requestFocusFromTouch, requestLayout, requestPointerCapture, requestRectangleOnScreen, requestRectangleOnScreen, requestUnbufferedDispatch, requestUnbufferedDispatch, requireViewById, resetPivot, resolveSize, resolveSizeAndState, restoreHierarchyState, saveAttributeDataForStyleable, saveHierarchyState, scheduleDrawable, scrollBy, scrollTo, sendAccessibilityEvent, sendAccessibilityEventUnchecked, setAccessibilityDataSensitive, setAccessibilityDelegate, setAccessibilityHeading, setAccessibilityLiveRegion, setAccessibilityPaneTitle, setAccessibilityTraversalAfter, setAccessibilityTraversalBefore, setActivated, setAllowClickWhenDisabled, setAllowedHandwritingDelegatePackage, setAllowedHandwritingDelegatorPackage, setAlpha, setAnimation, setAnimationMatrix, setAutofillHints, setAutofillId, setAutoHandwritingEnabled, setBackground, setBackgroundColor, setBackgroundDrawable, setBackgroundResource, setBackgroundTintBlendMode, setBackgroundTintList, setBackgroundTintMode, setBottom, setCameraDistance, setClickable, setClipBounds, setClipToOutline, setContentCaptureSession, setContentDescription, setContentSensitivity, setContextClickable, setDefaultFocusHighlightEnabled, setDrawingCacheBackgroundColor, setDrawingCacheEnabled, setDrawingCacheQuality, setDuplicateParentStateEnabled, setElevation, setEnabled, setFadingEdgeLength, setFilterTouchesWhenObscured, setFitsSystemWindows, setFocusable, setFocusable, setFocusableInTouchMode, setFocusedByDefault, setForceDarkAllowed, setForeground, setForegroundTintBlendMode, setForegroundTintList, setForegroundTintMode, setFrameContentVelocity, setHandwritingBoundsOffsets, setHandwritingDelegateFlags, setHandwritingDelegatorCallback, setHapticFeedbackEnabled, setHasTransientState, setHorizontalFadingEdgeEnabled, setHorizontalScrollBarEnabled, setHorizontalScrollbarThumbDrawable, setHorizontalScrollbarTrackDrawable, setHovered, setId, setImportantForAccessibility, setImportantForAutofill, setImportantForContentCapture, setIsCredential, setIsHandwritingDelegate, setKeepScreenOn, setKeyboardNavigationCluster, setLabelFor, setLayerPaint, setLayerType, setLayoutDirection, setLayoutParams, setLeft, setLeftTopRightBottom, setLongClickable, setMeasuredDimension, setMinimumHeight, setMinimumWidth, setNestedScrollingEnabled, setNextClusterForwardId, setNextFocusDownId, setNextFocusForwardId, setNextFocusLeftId, setNextFocusRightId, setNextFocusUpId, setOnApplyWindowInsetsListener, setOnCapturedPointerListener, setOnClickListener, setOnContextClickListener, setOnCreateContextMenuListener, setOnDragListener, setOnFocusChangeListener, setOnGenericMotionListener, setOnHoverListener, setOnKeyListener, setOnLongClickListener, setOnReceiveContentListener, setOnScrollChangeListener, setOnSystemUiVisibilityChangeListener, setOnTouchListener, setOutlineAmbientShadowColor, setOutlineProvider, setOutlineSpotShadowColor, setOverScrollMode, setPadding, setPaddingRelative, setPendingCredentialRequest, setPivotX, setPivotY, setPointerIcon, setPreferKeepClear, setPreferKeepClearRects, setPressed, setRenderEffect, setRevealOnFocusHint, setRight, setRotation, setRotationX, setRotationY, setSaveEnabled, setSaveFromParentEnabled, setScaleX, setScaleY, setScreenReaderFocusable, setScrollBarDefaultDelayBeforeFade, setScrollBarFadeDuration, setScrollbarFadingEnabled, setScrollBarSize, setScrollBarStyle, setScrollCaptureCallback, setScrollCaptureHint, setScrollContainer, setScrollIndicators, setScrollIndicators, setScrollX, setScrollY, setSelected, setSoundEffectsEnabled, setStateDescription, setStateListAnimator, setSupplementalDescription, setSystemGestureExclusionRects, setSystemUiVisibility, setTag, setTag, setTextAlignment, setTextDirection, setTooltipText, setTop, setTouchDelegate, setTransitionAlpha, setTransitionName, setTransitionVisibility, setTranslationX, setTranslationY, setTranslationZ, setVerticalFadingEdgeEnabled, setVerticalScrollBarEnabled, setVerticalScrollbarPosition, setVerticalScrollbarThumbDrawable, setVerticalScrollbarTrackDrawable, setViewTranslationCallback, setWillNotCacheDrawing, setWillNotDraw, setX, setY, setZ, showContextMenu, showContextMenu, startActionMode, startActionMode, startAnimation, startDrag, startDragAndDrop, startNestedScroll, stopNestedScroll, toString, transformMatrixToGlobal, transformMatrixToLocal, unscheduleDrawable, unscheduleDrawable, updateDragShadow, verifyDrawable, willNotCacheDrawing, willNotDraw</code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-android.view.ViewParent">Methods inherited from interface android.view.ViewParent</h3>
<code>canResolveLayoutDirection, canResolveTextAlignment, canResolveTextDirection, createContextMenu, getLayoutDirection, getParent, getParentForAccessibility, getTextAlignment, getTextDirection, isLayoutDirectionResolved, isLayoutRequested, isTextAlignmentResolved, isTextDirectionResolved, keyboardNavigationClusterSearch, requestFitSystemWindows, requestLayout</code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(android.content.Context,com.here.sdk.mapview.MapViewOptions)">
<h3>MapView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapView</span><wbr/><span className="parameters">(android.content.Context context,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options)</span></div>
<div className="block">Simple constructor to use when creating a map view from code.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Context the view is running in, through which it can access the current
 theme, resources, etc.</dd>
<dd><code>options</code> - Customization of view for example its map projection.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(android.content.Context)">
<h3>MapView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapView</span><wbr/><span className="parameters">(android.content.Context context)</span></div>
<div className="block">Simple constructor to use when creating a map view from code.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Context the view is running in, through which it can access the current
 theme, resources, etc.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(android.content.Context,android.util.AttributeSet)">
<h3>MapView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapView</span><wbr/><span className="parameters">(android.content.Context context,
 android.util.AttributeSet attrs)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Context the view is running in, through which it can access the current
 theme, resources, etc.</dd>
<dd><code>attrs</code> - A collection of attributes, as found associated with a tag in an XML document.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(android.content.Context,android.util.AttributeSet,int)">
<h3>MapView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapView</span><wbr/><span className="parameters">(android.content.Context context,
 android.util.AttributeSet attrs,
 int defStyleAttr)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - The Context the view is running in, through which it can access the current
 theme, resources, etc.</dd>
<dd><code>attrs</code> - A collection of attributes, as found associated with a tag in an XML document.</dd>
<dd><code>defStyleAttr</code> - An attribute in the current theme that contains a reference to a style
 resource that supplies defaults values for the StyledAttributes. Can be 0 to not look for
 defaults.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,android.content.Context,android.util.AttributeSet,int)">
<h3>MapView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapView</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 android.content.Context context,
 android.util.AttributeSet attrs,
 int defStyleAttr)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - The SDKNativeEngine instance.</dd>
<dd><code>context</code> - The Context the view is running in, through which it can access the current
 theme, resources, etc.</dd>
<dd><code>attrs</code> - A collection of attributes, as found associated with a tag in an XML document..</dd>
<dd><code>defStyleAttr</code> - An attribute in the current theme that contains a reference to a style
 resource that supplies defaults values for the StyledAttributes. Can be 0 to not look for
 defaults.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapview.MapViewOptions,android.content.Context,android.util.AttributeSet,int)">
<h3>MapView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapView</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewoptions" title="class in com.here.sdk.mapview">MapViewOptions</a> options,
 android.content.Context context,
 android.util.AttributeSet attrs,
 int defStyleAttr)</span></div>
<div className="block">Creates a new instance.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - The SDKNativeEngine instance.</dd>
<dd><code>options</code> - Customization of view for example its map projection.</dd>
<dd><code>context</code> - The Context the view is running in, through which it can access the current
 theme, resources, etc.</dd>
<dd><code>attrs</code> - A collection of attributes, as found associated with a tag in an XML document.</dd>
<dd><code>defStyleAttr</code> - An attribute in the current theme that contains a reference to a style
 resource that supplies defaults values for the StyledAttributes. Can be 0 to not look for
 defaults.</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="setVisibility(int)">
<h3>setVisibility</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVisibility</span><wbr/><span className="parameters">(int visibility)</span></div>
<div className="block">Sets the visibility of MapView. Visibilities of views pinned to
 MapView (see <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#pinView(android.view.View,com.here.sdk.core.GeoCoordinates)"><code>pinView(View, GeoCoordinates)</code></a>) will not be affected by this method.</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code>setVisibility</code> in class <code>android.view.View</code></dd>
<dt>Parameters:</dt>
<dd><code>visibility</code> - Desired visibility as one of <code>View.INVISIBLE</code>, <code>View.VISIBLE</code>
 or <code>View.GONE</code>.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPrimaryLanguage(com.here.sdk.core.LanguageCode)">
<h3>setPrimaryLanguage</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setPrimaryLanguage</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode)</span></div>
<div className="block">Set desired primary map display language for all instances of MapView.
 Applying a language change causes map to be redrawn.
 <p>
 If <code>null</code> is passed or the specified language is not supported, local language of the
 region will be used, which is the default behaviour.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>languageCode</code> - The code of the desired language, or <code>null</code> for default language.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setSecondaryLanguage(com.here.sdk.core.LanguageCode)">
<h3>setSecondaryLanguage</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setSecondaryLanguage</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode)</span></div>
<div className="block">Set desired secondary map display language for all instances of MapView.
 Applying a language change causes map to be redrawn.
 <p>
 If the specified language is not supported, local language of the region will be used.
 If null, no secondary map language will be used which is the default behaviour.
 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>languageCode</code> - The code of the desired language, or @null to unset.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPrimaryLanguage()">
<h3>getPrimaryLanguage</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span className="element-name">getPrimaryLanguage</span>()</div>
<div className="block">Gets code of currently set primary map display language.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The code of currently set language or @null language.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSecondaryLanguage()">
<h3>getSecondaryLanguage</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span className="element-name">getSecondaryLanguage</span>()</div>
<div className="block">Gets code of currently set secondary map display language.
 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The code of currently set language or @null language.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setShadowQuality(com.here.sdk.mapview.ShadowQuality)">
<h3>setShadowQuality</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type">void</span> <span className="element-name">setShadowQuality</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-shadowquality" title="enum class in com.here.sdk.mapview">ShadowQuality</a> shadowQuality)</span></div>
<div className="block">Set desired shadow quality for all instances of MapView/MapSurface.
 The quality controls the size of the shadow maps and the cascade count.
 The default shadow quality is <code>ShadowQuality.MEDIUM</code>.
 MapViews can request to render shadows by feature.
 Enabling shadows has a performance impact and should be considered only for devices with
 sufficient performance.
 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>shadowQuality</code> - The shadow quality.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getShadowQuality()">
<h3>getShadowQuality</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-shadowquality" title="enum class in com.here.sdk.mapview">ShadowQuality</a></span> <span className="element-name">getShadowQuality</span>()</div>
<div className="block">Gets the currently set shadow quality.
 The default shadow quality is <code>ShadowQuality.MEDIUM</code>.
 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The currently set shadow quality.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onCreate(android.os.Bundle)">
<h3>onCreate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onCreate</span><wbr/><span className="parameters">(android.os.Bundle bundle)</span></div>
<div className="block">Call this method in the onCreate() method of the lifecycle owner before calling any other
 MapView methods.

 <p>Note: <code>SDKNativeEngine</code> must be already initialized before calling this method.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>bundle</code> - The bundle which was passed to onCreate() method of the view owner</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onCreate(android.os.Bundle,java.lang.String)">
<h3>onCreate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onCreate</span><wbr/><span className="parameters">(android.os.Bundle bundle,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> identifier)</span></div>
<div className="block">Call this method in the onCreate() method of the lifecycle owner before calling any other
 MapView methods if there are multiple MapViews instances to (re)create.

 <p>Note: <code>SDKNativeEngine</code> must be already initialized before calling this method.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>bundle</code> - The bundle which was passed to onCreate() method of the view owner</dd>
<dd><code>identifier</code> - in case of multiple MapView instances use the same String which is passed
                   to onSaveInstanceState() to identify each MapView.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener)">
<h3>setOnReadyListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOnReadyListener</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview">MapView.OnReadyListener</a> readyListener)</span></div>
<div className="block">Sets the OnReadyListener, which will be notified once MapView initialization has
 been finished. It is highly recommended to put code that accesses map view related
 functionality inside <a href="sdk-for-android-navigate-mapview-onreadylistener#onMapViewReady()"><code>MapView.OnReadyListener.onMapViewReady()</code></a> instead of directly in
 <code>Activity</code>'s <code>onResume()</code>.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>readyListener</code> - The listener to be registered, or <code>null</code> to unregister any
                      previously register listener.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onResume()">
<h3>onResume</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onResume</span>()</div>
<div className="block">Call this method in the onResume() method of the lifecycle owner.</div>
</section>
</li>
<li>
<section className="detail" id="onPause()">
<h3>onPause</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onPause</span>()</div>
<div className="block">Call this method in the onPause() method of the lifecycle owner.</div>
</section>
</li>
<li>
<section className="detail" id="isValid()">
<h3>isValid</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isValid</span>()</div>
<div className="block">Returns whether this <code>MapView</code> is valid. An invalid <code>MapView</code> is non-functional.
 A <code>MapView</code> is considered valid only after
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle,java.lang.String)"><code>onCreate(Bundle, String)</code></a> and before
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onDestroy()"><code>onDestroy()</code></a> is called. <code>MapView</code> is also invalidated when the
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> it is using is destroyed.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#isValid()">isValid</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if this <code>MapView</code> is valid, <code>false</code> otherwise.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onDestroy()">
<h3>onDestroy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onDestroy</span>()</div>
<div className="block">Call this method in the onDestroy() method of the lifecycle owner</div>
</section>
</li>
<li>
<section className="detail" id="onSaveInstanceState(android.os.Bundle)">
<h3>onSaveInstanceState</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onSaveInstanceState</span><wbr/><span className="parameters">(android.os.Bundle bundle)</span></div>
<div className="block">Call this method in the onSaveInstance() method of the lifecycle owner.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>bundle</code> - the bundle which was passed to lifecycle owner</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onSaveInstanceState(android.os.Bundle,java.lang.String)">
<h3>onSaveInstanceState</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">onSaveInstanceState</span><wbr/><span className="parameters">(android.os.Bundle bundle,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> identifier)</span></div>
<div className="block">Call this method in the onSaveInstance() method of the lifecycle owner if multiple
 MapView instances are present. Each MapView instance should have its own identifier
 string which is passed to onSaveInstanceState() and onCreate() methods.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>bundle</code> - The bundle which was passed to lifecycle owner.</dd>
<dd><code>identifier</code> - If multiple MapView instances are under the same lifecycle owner then
                   provide a unique string to identify each MapView instance.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)">
<h3>pick</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">pick</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a> filter,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase-mappickcallback" title="interface in com.here.sdk.mapview">MapViewBase.MapPickCallback</a> callback)</span></div>
<div className="block"><p>Returns all map content located inside the specified pick area. Content to be picked is
 specified by a pick content filter.
 The pick area is defined by a rectangle in map view coordinates
 in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner
 of the map view.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)">pick</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>filter</code> - <p>Filter for the map content to be picked. When a filter is not set all of the
               pickable content will be picked.</p></dd>
<dd><code>viewArea</code> - <p>The rectangular pixel area of the view inside which map content will be
         picked.
     View area is relative to the map view's origin at (0, 0) at the top-left corner
     of the map view.</p></dd>
<dd><code>callback</code> - <p>Callback to call with the result. This will be called on a main thread
         when pick operation
     completes.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>geoToViewCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span className="element-name">geoToViewCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div className="block">Converts geographical coordinates to view coordinates (in pixels).
 <p>
 If specified, altitude of the input coordinates is interpreted as altitude above sea level.
 If not specified, the input coordinates are interpreted as being on ground elevation.
 The above distinction is only relevant when 3D terrain feature is enabled.
 
 The resulting view coordinates might be outside of current viewport, i.e. result might
 contain values less than zero or greater than view's dimensions.  If the render surface is
 not attached, it will return <code>null</code>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)">geoToViewCoordinates</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>Geographical coordinates to convert.</p></dd>
<dt>Returns:</dt>
<dd><p>The view coordinates of the specified geographical point or <code>null</code>
     if there is no render surface attached.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview"><code>MapView.OnReadyListener</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">
<h3>addLifecycleListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addLifecycleListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</span></div>
<div className="block">Adds a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> to this map view.
 Adding the same object multiple times has no effect.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">addLifecycleListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>lifecycleListener</code> - An object to be notified of lifecycle events.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">
<h3>removeLifecycleListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeLifecycleListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview">MapViewLifecycleListener</a> lifecycleListener)</span></div>
<div className="block">Removes a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a> from this map view.
 Trying to remove an object that was not added or was removed before
 has no effect.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)">removeLifecycleListener</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>lifecycleListener</code> - An object to stop being notified of lifecycle events.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="pinView(android.view.View,com.here.sdk.core.GeoCoordinates)">
<h3>pinView</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-viewpin" title="interface in com.here.sdk.mapview">MapView.ViewPin</a></span> <span className="element-name">pinView</span><wbr/><span className="parameters">(@NonNull
 android.view.View view,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block">Pins a <code>View</code> to the <code>MapView</code> and returns a proxy object that can be used to
 control the pinning.
 <p>
 Trying to pin a view that was already pinned or a view that has a parent
 has no effect and returns <code>null</code>.
 
 The altitude component of the coordinates, if set, is interpreted as above sea level.
 When not set, the coordinates are interpreted as at ground level.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - <code>View</code> to add.</dd>
<dd><code>coordinates</code> - <code>GeoCoordinates</code> to pin the view at.</dd>
<dt>Returns:</dt>
<dd>The handle to a pinned view, or <code>null</code> if the view could not be pinned to the
         map.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="unpinView(android.view.View)">
<h3>unpinView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">unpinView</span><wbr/><span className="parameters">(@NonNull
 android.view.View view)</span></div>
<div className="block">Removes a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-viewpin" title="interface in com.here.sdk.mapview"><code>MapView.ViewPin</code></a> from the <code>MapView</code> by specifying the corresponding view.
 Trying to unpin a view that was not pinned or was unpinned before has no effect.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - The view corresponding to the <code>ViewPin</code> to remove.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getViewPins()">
<h3>getViewPins</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-viewpin" title="interface in com.here.sdk.mapview">MapView.ViewPin</a>&gt;</span> <span className="element-name">getViewPins</span>()</div>
<div className="block">Returns a copy of the list of views currently pinned to the map view.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>A copy of the list of view pins.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="viewToGeoCoordinates(com.here.sdk.core.Point2D)">
<h3>viewToGeoCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">viewToGeoCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates)</span></div>
<div className="block">Converts view coordinates to geographical coordinates.
 <p>
 An optional altitude component of the resulting geographical coordinate is not set.
 
 If the view coordinates specify a point above a horizon, then the result
 is geographical coordinates of the point on a horizon below the specified
 view coordinates.
 
 The fog effect is ignored for the calculation, meaning that for the view point
 within the area covered by the fog, the result is geographical coordinates
 that would be displayed at the specified point if the fog effect was
 not applied.
 
 If the render surface is not attached, it will return <code>null</code>.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#viewToGeoCoordinates(com.here.sdk.core.Point2D)">viewToGeoCoordinates</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>viewCoordinates</code> - <p>Point inside the view to convert.</p></dd>
<dt>Returns:</dt>
<dd><p>The geographical coordinates under specified view point or <code>null</code>
         if there is no render surface attached.</p></dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-onreadylistener" title="interface in com.here.sdk.mapview"><code>MapView.OnReadyListener</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGestures()">
<h3>getGestures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures">Gestures</a></span> <span className="element-name">getGestures</span>()</div>
<div className="block">Returns the gestures control object</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getGestures()">getGestures</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-gestures-gestures" title="class in com.here.sdk.gestures"><code>Gestures</code></a> control object</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPixelScale()">
<h3>getPixelScale</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getPixelScale</span>()</div>
<div className="block">Gets the pixel scale factor used by this MapView.
 <p>
 It is is used to support screen resolution and size independence.
 This value is a derivative of the device's screen pixel density
 and is a direct analog of pixel density from DisplayMetrics.
 It can be used to translate between physical pixels and
 density independent pixels according to formula:
 dp = px / pixel_scale</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getPixelScale()">getPixelScale</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>current pixel scale factor, or 0.0 if MapView is not initialized</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getViewportSize()">
<h3>getViewportSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a></span> <span className="element-name">getViewportSize</span>()</div>
<div className="block">Gets the size of this map view in physical pixels.

 <p>If internally the map view's render surface is not attached yet
 (see: <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewlifecyclelistener" title="interface in com.here.sdk.mapview"><code>MapViewLifecycleListener</code></a>), or after the map view has been
 destroyed then a <code>Size2D</code> with zero width and height is returned.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getViewportSize()">getViewportSize</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>The viewport size in physical pixels, or Size2D(0.0,0.0) if MapView is not
 initialized</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFrameRate()">
<h3>getFrameRate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getFrameRate</span>()</div>
<div className="block">Gets maximum render frame rate in frames per second. The default value is 60 frames per
 second.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getFrameRate()">getFrameRate</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>Actual maximal render frame rate</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setFrameRate(int)">
<h3>setFrameRate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setFrameRate</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block">Sets maximum render frame rate in frames per second.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#setFrameRate(int)">setFrameRate</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - Maximum render frame rate in frames per second. Setting to 0 disables automatic
 rendering for this view. Setting negative values has no effect.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="takeScreenshot(com.here.sdk.mapview.MapView.TakeScreenshotCallback)">
<h3>takeScreenshot</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">takeScreenshot</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview-takescreenshotcallback" title="interface in com.here.sdk.mapview">MapView.TakeScreenshotCallback</a> callback)</span></div>
<div className="block">Asynchronously retrieves a screenshot of current map view.
 Note that this may not work when the map view is currently not visible, for example,
 when an application is running in background and onPause() was called.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - Completion handler called when the screenshot is completed</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)">
<h3>setWatermarkLocation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setWatermarkLocation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> offset)</span></div>
<div className="block"><p>Sets the position of the HERE logo watermark within the map view.

 By default, the watermark is aligned to the bottom-right corner of the view:
 Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2).
 It is recommended to change the default position only if necessary to avoid overlapping UI
 elements. The watermark should always be fully visible within the view. The anchor point on
 the watermark is its center (width/2, height/2), around which it will be placed in the map
 view. For map views smaller than 250 dip in both width and height, the watermark will not be
 shown.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)">setWatermarkLocation</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>anchor</code> - <p>Anchor point in normalized view coordinates [0, 1]. Map view's origin at
     (0, 0) indicates a top-left corner of the map view.
     Out of boundary anchor point values will be clamped to the [0, 1] range.</p></dd>
<dd><code>offset</code> - <p>A horizontal and vertical offset (expressed in positive/negative pixel
     coordinates) that allows shifting the watermark from the anchor point position in one or
     the other direction.
     For the quadrant of values expressing visible part of the map view negative offset shifts
     the watermark to the direction of the origin, positive - away from it.
     For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to
     the bottom.
     If specified offset will result in watermark being completely or partially out-of-view
     the offset will be adjusted internally so that watermark is fully visible.
     Offset is not being scaled when the map view size changes.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWatermarkSize()">
<h3>getWatermarkSize</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a></span> <span className="element-name">getWatermarkSize</span>()</div>
<div className="block"><p>Returns the watermark size in physical pixels.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getWatermarkSize()">getWatermarkSize</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>Provides the size of the watermark in physical pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCamera()">
<h3>getCamera</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera" title="class in com.here.sdk.mapview">MapCamera</a></span> <span className="element-name">getCamera</span>()</div>
<div className="block">Gets the camera control object for the map.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getCamera()">getCamera</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcamera" title="class in com.here.sdk.mapview"><code>MapCamera</code></a> object for the map.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMapScene()">
<h3>getMapScene</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview">MapScene</a></span> <span className="element-name">getMapScene</span>()</div>
<div className="block">Gets the map scene associated with this map view.
 <p>
 This can be used to request different map schemes to be displayed in the map view, and to
 add and remove map items from the map.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getMapScene()">getMapScene</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> associated with this map view.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called
 beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMapContext()">
<h3>getMapContext</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a></span> <span className="element-name">getMapContext</span>()</div>
<div className="block">Gets the map context associated with this map view.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getMapContext()">getMapContext</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> associated with this map view.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getHereMap()">
<h3>getHereMap</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview">HereMap</a></span> <span className="element-name">getHereMap</span>()</div>
<div className="block">Gets the HereMap associated with this map view.</div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-mapviewbase#getHereMap()">getHereMap</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a></code></dd>
<dt>Returns:</dt>
<dd>the <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a> associated with this map view.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle)"><code>onCreate(Bundle)</code></a> method was not called beforehand.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setFixedSize(int,int,double)">
<h3>setFixedSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setFixedSize</span><wbr/><span className="parameters">(int width,
 int height,
 double factor)</span></div>
<div className="block">Requests a fixed size to be used for rendering this MapView.

 Use this feature to render <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview"><code>MapView</code></a> to a smaller size and let the system upscale
 to actual on-screen size. The new fixed size is expected to have the same aspect ratio
 as the on-screen size and the factor provided to match the factor applied to the on-screen
 size that leads to the new fixed size:
 - width = on-screen width * factor
 - height = on-screen height * factor

 Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>width</code> - Fixed width to be used, in pixels.</dd>
<dd><code>height</code> - Fixed height to be used, in pixels.</dd>
<dd><code>factor</code> - Factor in between (0.0, 1.0] by which screen size differs from fixed size.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if factor is not inside (0.0, 1.0].</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html" title="class or interface in java.lang">UnsupportedOperationException</a></code> - if <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapview" title="class in com.here.sdk.mapview"><code>MapView</code></a> render mode is not
         MapRenderMode.SURFACE.</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
