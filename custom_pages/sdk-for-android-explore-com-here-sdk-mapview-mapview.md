---
title: "MapView (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapview"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object android.view.View android.view.ViewGroup
android.widget.FrameLayout com.here.sdk.mapview.MapView →
android.view.View android.view.ViewGroup android.widget.FrameLayout
com.here.sdk.mapview.MapView → android.view.ViewGroup
android.widget.FrameLayout com.here.sdk.mapview.MapView →
android.widget.FrameLayout com.here.sdk.mapview.MapView →
com.here.sdk.mapview.MapView

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
`android.graphics.drawable.Drawable.Callback, android.view.accessibility.AccessibilityEventSource, android.view.KeyEvent.Callback, android.view.ViewManager, android.view.ViewParent`,
[`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public class
</span><span class="element-name type-name-label">MapView</span>
<span class="extends-implements">extends android.widget.FrameLayout
implements
[MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")</span>

</div>

<div class="block">

A view that can display a map. The content of the map is controlled by
MapScene , which is accessible by calling getMapScene() . To display a
map, map scene needs to be loaded with MapScene.loadScene(MapScheme,
MapScene.LoadSceneCallback) . Manipulating the way the map is displayed
is possible using MapCamera , which is accessible by calling getCamera()
. Gesture handling can be modified through the Gestures object, which is
accessible by calling getGestures() . Permissions To use the MapView the
following application permissions need to be present:
android.permission.INTERNET and android.permission.ACCESS_NETWORK_STATE
Rendering mode MapView can draw the map using either SurfaceView or
TextureView . SurfaceView is the default method, offers best performance
and works best for single screen applications where there's a single
MapView which is not part of a complex view hierarchy and takes no part
in any UI animations. This method is known to cause graphical glitches
in some scenarios (like embedding multiple MapView s inside a view
pager), especially on Android 12 and newer. TextureView is less
performant, but behaves like any other view and can be easily
transformed and animated, making it a better fit for applications with
complex UI and/or multiple MapView s as part of a complex view
hierarchy. Rendering mode can only be set when creating a MapView , by
setting MapViewOptions.renderMode and passing the options to the
constructor. Coordinate systems When dealing with view coordinates,
physical pixels are used. MapView provides ways to translate between
view and geographic coordinates using viewToGeoCoordinates(Point2D) and
geoToViewCoordinates(GeoCoordinates) methods. Note that those two
methods only work when the MapView is fully ready, so if there is a need
to call them during lifecycle changes, they should be called from within
MapView.OnReadyListener.onMapViewReady() . See Lifecycle section below
for more details. Map caching Two caching mechanisms are supported.
First is in-memory cache, which keeps some number of map tiles around in
memory to avoid repeated network requests or storage reads. The second
mechanism is persistent cache that stores downloaded map data on the
device. Persistent cache requires storage permission to be granted.
Lifecycle For MapView to work correctly, it is required to call its
lifecycle methods from the owner Activity: onCreate(Bundle) , onResume()
, onPause() , onDestroy() and onSaveInstanceState(Bundle) . When dealing
with multiple MapView s in a single Activity, an extra identifier needs
to be passed to onCreate(Bundle, String) and onSaveInstanceState(Bundle,
String) . This identifier needs to be unique to all the MapView s owned
by the Activity and needs to be the same when recreating the Activity .
A MapView is considered valid only after onCreate(Bundle) or
onCreate(Bundle, String) and before onDestroy() is called. MapView is
also invalidated when the SDKNativeEngine it is using is destroyed.
isValid() can be used to check the state of MapView . MapView offers
additional lifecycle event exposed through MapView.OnReadyListener .
This can be used to determine when MapView is fully ready for action,
which means that map scene is loaded and drawing surface is ready to
render a map. This is important for coordinate conversion methods and
getViewportSize() , which work only when those conditions are met. When
OnReadyListener is set in Activity 's onCreate() before any other
operation is performed on the MapView , then
MapView.OnReadyListener.onMapViewReady() is called: after map scene is
successfully loaded for the first time some time after Activity 's
onResume() , assuming map scene had been loaded before Note: Before
using any API in this class, SDKNativeEngine must be already
initialized.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapView.OnReadyListener</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Listener that gets notified when MapView is fully initialized and
  ready to handle all operations, which means that map scene is loaded
  and drawing surface is ready to render a map.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static interface `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapview-takescreenshotcallback"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapView.TakeScreenshotCallback</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Callback to be called on retrieval of screenshot.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapView.ViewPin</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A ViewPin is used to display Android views at a fixed location on the
  map.

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class android.widget.FrameLayout

  `android.widget.FrameLayout.LayoutParams`

  </div>

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class android.view.ViewGroup

  `android.view.ViewGroup.MarginLayoutParams, android.view.ViewGroup.OnHierarchyChangeListener`

  </div>

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class android.view.View

  `android.view.View.AccessibilityDelegate, android.view.View.BaseSavedState, android.view.View.DragShadowBuilder, android.view.View.MeasureSpec, android.view.View.OnApplyWindowInsetsListener, android.view.View.OnAttachStateChangeListener, android.view.View.OnCapturedPointerListener, android.view.View.OnClickListener, android.view.View.OnContextClickListener, android.view.View.OnCreateContextMenuListener, android.view.View.OnDragListener, android.view.View.OnFocusChangeListener, android.view.View.OnGenericMotionListener, android.view.View.OnHoverListener, android.view.View.OnKeyListener, android.view.View.OnLayoutChangeListener, android.view.View.OnLongClickListener, android.view.View.OnScrollChangeListener, android.view.View.OnSystemUiVisibilityChangeListener, android.view.View.OnTouchListener, android.view.View.OnUnhandledKeyEventListener`

  </div>

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from interface com.here.sdk.mapview.[MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

  [`MapViewBase.MapPickCallback`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase-mappickcallback "interface in com.here.sdk.mapview")

  </div>

  </div>

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

  <div class="inherited-list">

  ### Fields inherited from class android.view.ViewGroup

  `CLIP_TO_PADDING_MASK, FOCUS_AFTER_DESCENDANTS, FOCUS_BEFORE_DESCENDANTS, FOCUS_BLOCK_DESCENDANTS, LAYOUT_MODE_CLIP_BOUNDS, LAYOUT_MODE_OPTICAL_BOUNDS, PERSISTENT_ALL_CACHES, PERSISTENT_ANIMATION_CACHE, PERSISTENT_NO_CACHE, PERSISTENT_SCROLLING_CACHE`

  </div>

  <div class="inherited-list">

  ### Fields inherited from class android.view.View

  `ACCESSIBILITY_DATA_SENSITIVE_AUTO, ACCESSIBILITY_DATA_SENSITIVE_NO, ACCESSIBILITY_DATA_SENSITIVE_YES, ACCESSIBILITY_LIVE_REGION_ASSERTIVE, ACCESSIBILITY_LIVE_REGION_NONE, ACCESSIBILITY_LIVE_REGION_POLITE, ALPHA, AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR, AUTOFILL_HINT_CREDIT_CARD_NUMBER, AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE, AUTOFILL_HINT_EMAIL_ADDRESS, AUTOFILL_HINT_NAME, AUTOFILL_HINT_PASSWORD, AUTOFILL_HINT_PHONE, AUTOFILL_HINT_POSTAL_ADDRESS, AUTOFILL_HINT_POSTAL_CODE, AUTOFILL_HINT_USERNAME, AUTOFILL_TYPE_DATE, AUTOFILL_TYPE_LIST, AUTOFILL_TYPE_NONE, AUTOFILL_TYPE_TEXT, AUTOFILL_TYPE_TOGGLE, CONTENT_SENSITIVITY_AUTO, CONTENT_SENSITIVITY_NOT_SENSITIVE, CONTENT_SENSITIVITY_SENSITIVE, DRAG_FLAG_ACCESSIBILITY_ACTION, DRAG_FLAG_GLOBAL, DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION, DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION, DRAG_FLAG_GLOBAL_SAME_APPLICATION, DRAG_FLAG_GLOBAL_URI_READ, DRAG_FLAG_GLOBAL_URI_WRITE, DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START, DRAG_FLAG_OPAQUE, DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG, DRAWING_CACHE_QUALITY_AUTO, DRAWING_CACHE_QUALITY_HIGH, DRAWING_CACHE_QUALITY_LOW, EMPTY_STATE_SET, ENABLED_FOCUSED_SELECTED_STATE_SET, ENABLED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, ENABLED_FOCUSED_STATE_SET, ENABLED_FOCUSED_WINDOW_FOCUSED_STATE_SET, ENABLED_SELECTED_STATE_SET, ENABLED_SELECTED_WINDOW_FOCUSED_STATE_SET, ENABLED_STATE_SET, ENABLED_WINDOW_FOCUSED_STATE_SET, FIND_VIEWS_WITH_CONTENT_DESCRIPTION, FIND_VIEWS_WITH_TEXT, FOCUS_BACKWARD, FOCUS_DOWN, FOCUS_FORWARD, FOCUS_LEFT, FOCUS_RIGHT, FOCUS_UP, FOCUSABLE, FOCUSABLE_AUTO, FOCUSABLES_ALL, FOCUSABLES_TOUCH_MODE, FOCUSED_SELECTED_STATE_SET, FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, FOCUSED_STATE_SET, FOCUSED_WINDOW_FOCUSED_STATE_SET, GONE, HAPTIC_FEEDBACK_ENABLED, IMPORTANT_FOR_ACCESSIBILITY_AUTO, IMPORTANT_FOR_ACCESSIBILITY_NO, IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS, IMPORTANT_FOR_ACCESSIBILITY_YES, IMPORTANT_FOR_AUTOFILL_AUTO, IMPORTANT_FOR_AUTOFILL_NO, IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_AUTOFILL_YES, IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_CONTENT_CAPTURE_AUTO, IMPORTANT_FOR_CONTENT_CAPTURE_NO, IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_CONTENT_CAPTURE_YES, IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS, INVISIBLE, KEEP_SCREEN_ON, LAYER_TYPE_HARDWARE, LAYER_TYPE_NONE, LAYER_TYPE_SOFTWARE, LAYOUT_DIRECTION_INHERIT, LAYOUT_DIRECTION_LOCALE, LAYOUT_DIRECTION_LTR, LAYOUT_DIRECTION_RTL, MEASURED_HEIGHT_STATE_SHIFT, MEASURED_SIZE_MASK, MEASURED_STATE_MASK, MEASURED_STATE_TOO_SMALL, NO_ID, NOT_FOCUSABLE, OVER_SCROLL_ALWAYS, OVER_SCROLL_IF_CONTENT_SCROLLS, OVER_SCROLL_NEVER, PRESSED_ENABLED_FOCUSED_SELECTED_STATE_SET, PRESSED_ENABLED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_FOCUSED_STATE_SET, PRESSED_ENABLED_FOCUSED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_SELECTED_STATE_SET, PRESSED_ENABLED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_STATE_SET, PRESSED_ENABLED_WINDOW_FOCUSED_STATE_SET, PRESSED_FOCUSED_SELECTED_STATE_SET, PRESSED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_FOCUSED_STATE_SET, PRESSED_FOCUSED_WINDOW_FOCUSED_STATE_SET, PRESSED_SELECTED_STATE_SET, PRESSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_STATE_SET, PRESSED_WINDOW_FOCUSED_STATE_SET, REQUESTED_FRAME_RATE_CATEGORY_DEFAULT, REQUESTED_FRAME_RATE_CATEGORY_HIGH, REQUESTED_FRAME_RATE_CATEGORY_LOW, REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE, REQUESTED_FRAME_RATE_CATEGORY_NORMAL, ROTATION, ROTATION_X, ROTATION_Y, SCALE_X, SCALE_Y, SCREEN_STATE_OFF, SCREEN_STATE_ON, SCROLL_AXIS_HORIZONTAL, SCROLL_AXIS_NONE, SCROLL_AXIS_VERTICAL, SCROLL_CAPTURE_HINT_AUTO, SCROLL_CAPTURE_HINT_EXCLUDE, SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS, SCROLL_CAPTURE_HINT_INCLUDE, SCROLL_INDICATOR_BOTTOM, SCROLL_INDICATOR_END, SCROLL_INDICATOR_LEFT, SCROLL_INDICATOR_RIGHT, SCROLL_INDICATOR_START, SCROLL_INDICATOR_TOP, SCROLLBAR_POSITION_DEFAULT, SCROLLBAR_POSITION_LEFT, SCROLLBAR_POSITION_RIGHT, SCROLLBARS_INSIDE_INSET, SCROLLBARS_INSIDE_OVERLAY, SCROLLBARS_OUTSIDE_INSET, SCROLLBARS_OUTSIDE_OVERLAY, SELECTED_STATE_SET, SELECTED_WINDOW_FOCUSED_STATE_SET, SOUND_EFFECTS_ENABLED, STATUS_BAR_HIDDEN, STATUS_BAR_VISIBLE, SYSTEM_UI_FLAG_FULLSCREEN, SYSTEM_UI_FLAG_HIDE_NAVIGATION, SYSTEM_UI_FLAG_IMMERSIVE, SYSTEM_UI_FLAG_IMMERSIVE_STICKY, SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN, SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION, SYSTEM_UI_FLAG_LAYOUT_STABLE, SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR, SYSTEM_UI_FLAG_LIGHT_STATUS_BAR, SYSTEM_UI_FLAG_LOW_PROFILE, SYSTEM_UI_FLAG_VISIBLE, SYSTEM_UI_LAYOUT_FLAGS, TEXT_ALIGNMENT_CENTER, TEXT_ALIGNMENT_GRAVITY, TEXT_ALIGNMENT_INHERIT, TEXT_ALIGNMENT_TEXT_END, TEXT_ALIGNMENT_TEXT_START, TEXT_ALIGNMENT_VIEW_END, TEXT_ALIGNMENT_VIEW_START, TEXT_DIRECTION_ANY_RTL, TEXT_DIRECTION_FIRST_STRONG, TEXT_DIRECTION_FIRST_STRONG_LTR, TEXT_DIRECTION_FIRST_STRONG_RTL, TEXT_DIRECTION_INHERIT, TEXT_DIRECTION_LOCALE, TEXT_DIRECTION_LTR, TEXT_DIRECTION_RTL, TRANSLATION_X, TRANSLATION_Y, TRANSLATION_Z, VIEW_LOG_TAG, VISIBLE, WINDOW_FOCUSED_STATE_SET, X, Y, Z`

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      MapView (android.content.Context context)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Simple constructor to use when creating a map view from code.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapView (android.content.Context context,
       android.util.AttributeSet attrs)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapView (android.content.Context context,
       android.util.AttributeSet attrs,
       int defStyleAttr)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapView (android.content.Context context, MapViewOptions options)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Simple constructor to use when creating a map view from code.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapView ( SDKNativeEngine engine,
       android.content.Context context,
       android.util.AttributeSet attrs,
       int defStyleAttr)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapView ( SDKNativeEngine engine, MapViewOptions options,
       android.content.Context context,
       android.util.AttributeSet attrs,
       int defStyleAttr)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addLifecycleListener ( MapViewLifecycleListener lifecycleListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a MapViewLifecycleListener to this map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Point2D`](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      geoToViewCoordinates ( GeoCoordinates geoCoordinates)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts geographical coordinates to view coordinates (in pixels).

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapCamera`](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCamera ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the camera control object for the map.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFrameRate ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets maximum render frame rate in frames per second.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Gestures`](sdk-for-android-explore-com-here-sdk-gestures-gestures "class in com.here.sdk.gestures")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGestures ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the gestures control object

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`HereMap`](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getHereMap ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the HereMap associated with this map view.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapContext`](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMapContext ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map context associated with this map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapScene`](sdk-for-android-explore-com-here-sdk-mapview-mapscene "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMapScene ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map scene associated with this map view.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPixelScale ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the pixel scale factor used by this MapView.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`LanguageCode`](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getPrimaryLanguage ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets code of currently set primary map display language.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`LanguageCode`](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getSecondaryLanguage ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets code of currently set secondary map display language.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`ShadowQuality`](sdk-for-android-explore-com-here-sdk-mapview-shadowquality "enum class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getShadowQuality ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets the currently set shadow quality.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`MapView.ViewPin`](sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin "interface in com.here.sdk.mapview")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getViewPins ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a copy of the list of views currently pinned to the map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Size2D`](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getViewportSize ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the size of this map view in physical pixels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Size2D`](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWatermarkSize ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the watermark size in physical pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isValid ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns whether this MapView is valid.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onCreate (android.os.Bundle bundle)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onCreate() method of the lifecycle owner
  before calling any other MapView methods.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onCreate (android.os.Bundle bundle, String identifier)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onCreate() method of the lifecycle owner
  before calling any other MapView methods if there are multiple
  MapViews instances to (re)create.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onDestroy ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onDestroy() method of the lifecycle owner

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onPause ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onPause() method of the lifecycle owner.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onResume ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onResume() method of the lifecycle owner.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onSaveInstanceState (android.os.Bundle bundle)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onSaveInstance() method of the lifecycle
  owner.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onSaveInstanceState (android.os.Bundle bundle, String identifier)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Call this method in the onSaveInstance() method of the lifecycle owner
  if multiple MapView instances are present.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      pick ( MapScene.MapPickFilter filter, Rectangle2D viewArea, MapViewBase.MapPickCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns all map content located inside the specified pick area.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapView.ViewPin`](sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin "interface in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      pinView (android.view.View view, GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Pins a View to the MapView and returns a proxy object that can be used
  to control the pinning.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeLifecycleListener ( MapViewLifecycleListener lifecycleListener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a MapViewLifecycleListener from this map view.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setFixedSize (int width,
       int height,
       double factor)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Requests a fixed size to be used for rendering this MapView.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setFrameRate (int value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets maximum render frame rate in frames per second.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOnReadyListener ( MapView.OnReadyListener readyListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the OnReadyListener, which will be notified once MapView
  initialization has been finished.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setPrimaryLanguage ( LanguageCode languageCode)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Set desired primary map display language for all instances of MapView.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setSecondaryLanguage ( LanguageCode languageCode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Set desired secondary map display language for all instances of
  MapView.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setShadowQuality ( ShadowQuality shadowQuality)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Set desired shadow quality for all instances of MapView/MapSurface.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVisibility (int visibility)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the visibility of MapView.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setWatermarkLocation ( Anchor2D anchor, Point2D offset)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the position of the HERE logo watermark within the map view.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      takeScreenshot ( MapView.TakeScreenshotCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously retrieves a screenshot of current map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      unpinView (android.view.View view)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a MapView.ViewPin from the MapView by specifying the
  corresponding view.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      viewToGeoCoordinates ( Point2D viewCoordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts view coordinates to geographical coordinates.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class android.widget.FrameLayout

  `checkLayoutParams, generateDefaultLayoutParams, generateLayoutParams, generateLayoutParams, getAccessibilityClassName, getConsiderGoneChildrenWhenMeasuring, getMeasureAllChildren, onLayout, onMeasure, setForegroundGravity, setMeasureAllChildren, shouldDelayChildPressedState`

  </div>

  <div class="inherited-list">

  ### Methods inherited from class android.view.ViewGroup

  `addChildrenForAccessibility, addExtraDataToAccessibilityNodeInfo, addFocusables, addKeyboardNavigationClusters, addStatesFromChildren, addTouchables, addView, addView, addView, addView, addView, addViewInLayout, addViewInLayout, attachLayoutAnimationParameters, attachViewToParent, bringChildToFront, canAnimate, childDrawableStateChanged, childHasTransientStateChanged, cleanupLayoutState, clearChildFocus, clearDisappearingChildren, clearFocus, debug, detachAllViewsFromParent, detachViewFromParent, detachViewFromParent, detachViewsFromParent, dispatchApplyWindowInsets, dispatchCapturedPointerEvent, dispatchConfigurationChanged, dispatchCreateViewTranslationRequest, dispatchDisplayHint, dispatchDragEvent, dispatchDraw, dispatchDrawableHotspotChanged, dispatchFinishTemporaryDetach, dispatchFreezeSelfOnly, dispatchGenericFocusedEvent, dispatchGenericPointerEvent, dispatchHoverEvent, dispatchKeyEvent, dispatchKeyEventPreIme, dispatchKeyShortcutEvent, dispatchPointerCaptureChanged, dispatchProvideAutofillStructure, dispatchProvideStructure, dispatchRestoreInstanceState, dispatchSaveInstanceState, dispatchScrollCaptureSearch, dispatchSetActivated, dispatchSetPressed, dispatchSetSelected, dispatchStartTemporaryDetach, dispatchSystemUiVisibilityChanged, dispatchThawSelfOnly, dispatchTouchEvent, dispatchTrackballEvent, dispatchUnhandledMove, dispatchVisibilityChanged, dispatchWindowFocusChanged, dispatchWindowInsetsAnimationEnd, dispatchWindowInsetsAnimationPrepare, dispatchWindowInsetsAnimationProgress, dispatchWindowInsetsAnimationStart, dispatchWindowSystemUiVisiblityChanged, dispatchWindowVisibilityChanged, drawableStateChanged, drawChild, endViewTransition, findFocus, findOnBackInvokedDispatcherForChild, findViewsWithText, focusableViewAvailable, focusSearch, gatherTransparentRegion, getChildAt, getChildCount, getChildDrawingOrder, getChildDrawingOrder, getChildMeasureSpec, getChildStaticTransformation, getChildVisibleRect, getClipChildren, getClipToPadding, getDescendantFocusability, getFocusedChild, getLayoutAnimation, getLayoutAnimationListener, getLayoutMode, getLayoutTransition, getNestedScrollAxes, getOverlay, getPersistentDrawingCache, getTouchscreenBlocksFocus, hasFocus, hasTransientState, indexOfChild, invalidateChild, invalidateChildInParent, isAlwaysDrawnWithCacheEnabled, isAnimationCacheEnabled, isChildrenDrawingOrderEnabled, isChildrenDrawnWithCacheEnabled, isLayoutSuppressed, isMotionEventSplittingEnabled, isTransitionGroup, jumpDrawablesToCurrentState, layout, measureChild, measureChildren, measureChildWithMargins, notifySubtreeAccessibilityStateChanged, offsetDescendantRectToMyCoords, offsetRectIntoDescendantCoords, onAttachedToWindow, onCreateDrawableState, onDescendantInvalidated, onDetachedFromWindow, onInterceptHoverEvent, onInterceptTouchEvent, onNestedFling, onNestedPreFling, onNestedPrePerformAccessibilityAction, onNestedPreScroll, onNestedScroll, onNestedScrollAccepted, onRequestFocusInDescendants, onRequestSendAccessibilityEvent, onResolvePointerIcon, onStartNestedScroll, onStopNestedScroll, onViewAdded, onViewRemoved, propagateRequestedFrameRate, recomputeViewAttributes, removeAllViews, removeAllViewsInLayout, removeDetachedView, removeView, removeViewAt, removeViewInLayout, removeViews, removeViewsInLayout, requestChildFocus, requestChildRectangleOnScreen, requestDisallowInterceptTouchEvent, requestFocus, requestSendAccessibilityEvent, requestTransparentRegion, restoreDefaultFocus, scheduleLayoutAnimation, setAddStatesFromChildren, setAlwaysDrawnWithCacheEnabled, setAnimationCacheEnabled, setChildrenDrawingCacheEnabled, setChildrenDrawingOrderEnabled, setChildrenDrawnWithCacheEnabled, setClipChildren, setClipToPadding, setDescendantFocusability, setLayoutAnimation, setLayoutAnimationListener, setLayoutMode, setLayoutTransition, setMotionEventSplittingEnabled, setOnHierarchyChangeListener, setPersistentDrawingCache, setRequestedFrameRate, setStaticTransformationsEnabled, setTouchscreenBlocksFocus, setTransitionGroup, setWindowInsetsAnimationCallback, showContextMenuForChild, showContextMenuForChild, startActionModeForChild, startActionModeForChild, startLayoutAnimation, startViewTransition, suppressLayout, updateViewLayout`

  </div>

  <div class="inherited-list">

  ### Methods inherited from class android.view.View

  `addFocusables, addOnAttachStateChangeListener, addOnLayoutChangeListener, addOnUnhandledKeyEventListener, animate, announceForAccessibility, autofill, autofill, awakenScrollBars, awakenScrollBars, awakenScrollBars, bringToFront, buildDrawingCache, buildDrawingCache, buildLayer, callOnClick, cancelDragAndDrop, cancelLongPress, cancelPendingInputEvents, canResolveLayoutDirection, canResolveTextAlignment, canResolveTextDirection, canScrollHorizontally, canScrollVertically, checkInputConnectionProxy, clearAnimation, clearPendingCredentialRequest, clearViewTranslationCallback, combineMeasuredStates, computeHorizontalScrollExtent, computeHorizontalScrollOffset, computeHorizontalScrollRange, computeScroll, computeSystemWindowInsets, computeVerticalScrollExtent, computeVerticalScrollOffset, computeVerticalScrollRange, createAccessibilityNodeInfo, createContextMenu, destroyDrawingCache, dispatchGenericMotionEvent, dispatchNestedFling, dispatchNestedPreFling, dispatchNestedPrePerformAccessibilityAction, dispatchNestedPreScroll, dispatchNestedScroll, dispatchPopulateAccessibilityEvent, draw, drawableHotspotChanged, findOnBackInvokedDispatcher, findViewById, findViewWithTag, fitSystemWindows, focusSearch, forceHasOverlappingRendering, forceLayout, generateDisplayHash, generateViewId, getAccessibilityDelegate, getAccessibilityLiveRegion, getAccessibilityNodeProvider, getAccessibilityPaneTitle, getAccessibilityTraversalAfter, getAccessibilityTraversalBefore, getAllowedHandwritingDelegatePackageName, getAllowedHandwritingDelegatorPackageName, getAlpha, getAnimation, getAnimationMatrix, getApplicationWindowToken, getAttributeResolutionStack, getAttributeSourceResourceMap, getAutofillHints, getAutofillId, getAutofillType, getAutofillValue, getBackground, getBackgroundTintBlendMode, getBackgroundTintList, getBackgroundTintMode, getBaseline, getBottom, getBottomFadingEdgeStrength, getBottomPaddingOffset, getCameraDistance, getClipBounds, getClipBounds, getClipToOutline, getContentCaptureSession, getContentDescription, getContentSensitivity, getContext, getContextMenuInfo, getDefaultFocusHighlightEnabled, getDefaultSize, getDisplay, getDrawableState, getDrawingCache, getDrawingCache, getDrawingCacheBackgroundColor, getDrawingCacheQuality, getDrawingRect, getDrawingTime, getElevation, getExplicitStyle, getFilterTouchesWhenObscured, getFitsSystemWindows, getFocusable, getFocusables, getFocusedRect, getForeground, getForegroundGravity, getForegroundTintBlendMode, getForegroundTintList, getForegroundTintMode, getFrameContentVelocity, getGlobalVisibleRect, getGlobalVisibleRect, getHandler, getHandwritingBoundsOffsetBottom, getHandwritingBoundsOffsetLeft, getHandwritingBoundsOffsetRight, getHandwritingBoundsOffsetTop, getHandwritingDelegateFlags, getHandwritingDelegatorCallback, getHasOverlappingRendering, getHeight, getHitRect, getHorizontalFadingEdgeLength, getHorizontalScrollbarHeight, getHorizontalScrollbarThumbDrawable, getHorizontalScrollbarTrackDrawable, getId, getImportantForAccessibility, getImportantForAutofill, getImportantForContentCapture, getKeepScreenOn, getKeyDispatcherState, getLabelFor, getLayerType, getLayoutDirection, getLayoutParams, getLeft, getLeftFadingEdgeStrength, getLeftPaddingOffset, getLocalVisibleRect, getLocationInSurface, getLocationInWindow, getLocationOnScreen, getMatrix, getMeasuredHeight, getMeasuredHeightAndState, getMeasuredState, getMeasuredWidth, getMeasuredWidthAndState, getMinimumHeight, getMinimumWidth, getNextClusterForwardId, getNextFocusDownId, getNextFocusForwardId, getNextFocusLeftId, getNextFocusRightId, getNextFocusUpId, getOnFocusChangeListener, getOutlineAmbientShadowColor, getOutlineProvider, getOutlineSpotShadowColor, getOverScrollMode, getPaddingBottom, getPaddingEnd, getPaddingLeft, getPaddingRight, getPaddingStart, getPaddingTop, getParent, getParentForAccessibility, getPendingCredentialCallback, getPendingCredentialRequest, getPivotX, getPivotY, getPointerIcon, getPreferKeepClearRects, getReceiveContentMimeTypes, getRequestedFrameRate, getResources, getRevealOnFocusHint, getRight, getRightFadingEdgeStrength, getRightPaddingOffset, getRootSurfaceControl, getRootView, getRootWindowInsets, getRotation, getRotationX, getRotationY, getScaleX, getScaleY, getScrollBarDefaultDelayBeforeFade, getScrollBarFadeDuration, getScrollBarSize, getScrollBarStyle, getScrollCaptureHint, getScrollIndicators, getScrollX, getScrollY, getSolidColor, getSourceLayoutResId, getStateDescription, getStateListAnimator, getSuggestedMinimumHeight, getSuggestedMinimumWidth, getSupplementalDescription, getSystemGestureExclusionRects, getSystemUiVisibility, getTag, getTag, getTextAlignment, getTextDirection, getTooltipText, getTop, getTopFadingEdgeStrength, getTopPaddingOffset, getTouchables, getTouchDelegate, getTransitionAlpha, getTransitionName, getTranslationX, getTranslationY, getTranslationZ, getUniqueDrawingId, getVerticalFadingEdgeLength, getVerticalScrollbarPosition, getVerticalScrollbarThumbDrawable, getVerticalScrollbarTrackDrawable, getVerticalScrollbarWidth, getViewTranslationResponse, getViewTreeObserver, getVisibility, getWidth, getWindowAttachCount, getWindowId, getWindowInsetsController, getWindowSystemUiVisibility, getWindowToken, getWindowVisibility, getWindowVisibleDisplayFrame, getX, getY, getZ, hasExplicitFocusable, hasFocusable, hasNestedScrollingParent, hasOnClickListeners, hasOnLongClickListeners, hasOverlappingRendering, hasPointerCapture, hasWindowFocus, inflate, invalidate, invalidate, invalidate, invalidateDrawable, invalidateOutline, isAccessibilityDataSensitive, isAccessibilityFocused, isAccessibilityHeading, isActivated, isAttachedToWindow, isAutoHandwritingEnabled, isClickable, isContentSensitive, isContextClickable, isCredential, isDirty, isDrawingCacheEnabled, isDuplicateParentStateEnabled, isEnabled, isFocusable, isFocusableInTouchMode, isFocused, isFocusedByDefault, isForceDarkAllowed, isHandwritingDelegate, isHapticFeedbackEnabled, isHardwareAccelerated, isHorizontalFadingEdgeEnabled, isHorizontalScrollBarEnabled, isHovered, isImportantForAccessibility, isImportantForAutofill, isImportantForContentCapture, isInEditMode, isInLayout, isInTouchMode, isKeyboardNavigationCluster, isLaidOut, isLayoutDirectionResolved, isLayoutRequested, isLongClickable, isNestedScrollingEnabled, isOpaque, isPaddingOffsetRequired, isPaddingRelative, isPivotSet, isPreferKeepClear, isPressed, isSaveEnabled, isSaveFromParentEnabled, isScreenReaderFocusable, isScrollbarFadingEnabled, isScrollContainer, isSelected, isShowingLayoutBounds, isShown, isSoundEffectsEnabled, isTemporarilyDetached, isTextAlignmentResolved, isTextDirectionResolved, isVerticalFadingEdgeEnabled, isVerticalScrollBarEnabled, isVisibleToUserForAutofill, keyboardNavigationClusterSearch, measure, mergeDrawableStates, offsetLeftAndRight, offsetTopAndBottom, onAnimationEnd, onAnimationStart, onApplyWindowInsets, onCancelPendingInputEvents, onCapturedPointerEvent, onCheckIsTextEditor, onConfigurationChanged, onCreateContextMenu, onCreateInputConnection, onCreateViewTranslationRequest, onCreateVirtualViewTranslationRequests, onDisplayHint, onDragEvent, onDraw, onDrawForeground, onDrawScrollBars, onFilterTouchEventForSecurity, onFinishInflate, onFinishTemporaryDetach, onFocusChanged, onGenericMotionEvent, onHoverChanged, onHoverEvent, onInitializeAccessibilityEvent, onInitializeAccessibilityNodeInfo, onKeyDown, onKeyLongPress, onKeyMultiple, onKeyPreIme, onKeyShortcut, onKeyUp, onOverScrolled, onPointerCaptureChange, onPopulateAccessibilityEvent, onProvideAutofillStructure, onProvideAutofillVirtualStructure, onProvideContentCaptureStructure, onProvideStructure, onProvideVirtualStructure, onReceiveContent, onRestoreInstanceState, onRtlPropertiesChanged, onSaveInstanceState, onScreenStateChanged, onScrollCaptureSearch, onScrollChanged, onSetAlpha, onSizeChanged, onStartTemporaryDetach, onTrackballEvent, onViewTranslationResponse, onVirtualViewTranslationResponses, onVisibilityAggregated, onVisibilityChanged, onWindowFocusChanged, onWindowSystemUiVisibilityChanged, onWindowVisibilityChanged, overScrollBy, performAccessibilityAction, performClick, performContextClick, performContextClick, performHapticFeedback, performHapticFeedback, performLongClick, performLongClick, performReceiveContent, playSoundEffect, post, postDelayed, postInvalidate, postInvalidate, postInvalidateDelayed, postInvalidateDelayed, postInvalidateOnAnimation, postInvalidateOnAnimation, postOnAnimation, postOnAnimationDelayed, refreshDrawableState, releasePointerCapture, removeCallbacks, removeOnAttachStateChangeListener, removeOnLayoutChangeListener, removeOnUnhandledKeyEventListener, reportAppJankStats, requestApplyInsets, requestFitSystemWindows, requestFocus, requestFocus, requestFocusFromTouch, requestLayout, requestPointerCapture, requestRectangleOnScreen, requestRectangleOnScreen, requestUnbufferedDispatch, requestUnbufferedDispatch, requireViewById, resetPivot, resolveSize, resolveSizeAndState, restoreHierarchyState, saveAttributeDataForStyleable, saveHierarchyState, scheduleDrawable, scrollBy, scrollTo, sendAccessibilityEvent, sendAccessibilityEventUnchecked, setAccessibilityDataSensitive, setAccessibilityDelegate, setAccessibilityHeading, setAccessibilityLiveRegion, setAccessibilityPaneTitle, setAccessibilityTraversalAfter, setAccessibilityTraversalBefore, setActivated, setAllowClickWhenDisabled, setAllowedHandwritingDelegatePackage, setAllowedHandwritingDelegatorPackage, setAlpha, setAnimation, setAnimationMatrix, setAutofillHints, setAutofillId, setAutoHandwritingEnabled, setBackground, setBackgroundColor, setBackgroundDrawable, setBackgroundResource, setBackgroundTintBlendMode, setBackgroundTintList, setBackgroundTintMode, setBottom, setCameraDistance, setClickable, setClipBounds, setClipToOutline, setContentCaptureSession, setContentDescription, setContentSensitivity, setContextClickable, setDefaultFocusHighlightEnabled, setDrawingCacheBackgroundColor, setDrawingCacheEnabled, setDrawingCacheQuality, setDuplicateParentStateEnabled, setElevation, setEnabled, setFadingEdgeLength, setFilterTouchesWhenObscured, setFitsSystemWindows, setFocusable, setFocusable, setFocusableInTouchMode, setFocusedByDefault, setForceDarkAllowed, setForeground, setForegroundTintBlendMode, setForegroundTintList, setForegroundTintMode, setFrameContentVelocity, setHandwritingBoundsOffsets, setHandwritingDelegateFlags, setHandwritingDelegatorCallback, setHapticFeedbackEnabled, setHasTransientState, setHorizontalFadingEdgeEnabled, setHorizontalScrollBarEnabled, setHorizontalScrollbarThumbDrawable, setHorizontalScrollbarTrackDrawable, setHovered, setId, setImportantForAccessibility, setImportantForAutofill, setImportantForContentCapture, setIsCredential, setIsHandwritingDelegate, setKeepScreenOn, setKeyboardNavigationCluster, setLabelFor, setLayerPaint, setLayerType, setLayoutDirection, setLayoutParams, setLeft, setLeftTopRightBottom, setLongClickable, setMeasuredDimension, setMinimumHeight, setMinimumWidth, setNestedScrollingEnabled, setNextClusterForwardId, setNextFocusDownId, setNextFocusForwardId, setNextFocusLeftId, setNextFocusRightId, setNextFocusUpId, setOnApplyWindowInsetsListener, setOnCapturedPointerListener, setOnClickListener, setOnContextClickListener, setOnCreateContextMenuListener, setOnDragListener, setOnFocusChangeListener, setOnGenericMotionListener, setOnHoverListener, setOnKeyListener, setOnLongClickListener, setOnReceiveContentListener, setOnScrollChangeListener, setOnSystemUiVisibilityChangeListener, setOnTouchListener, setOutlineAmbientShadowColor, setOutlineProvider, setOutlineSpotShadowColor, setOverScrollMode, setPadding, setPaddingRelative, setPendingCredentialRequest, setPivotX, setPivotY, setPointerIcon, setPreferKeepClear, setPreferKeepClearRects, setPressed, setRenderEffect, setRevealOnFocusHint, setRight, setRotation, setRotationX, setRotationY, setSaveEnabled, setSaveFromParentEnabled, setScaleX, setScaleY, setScreenReaderFocusable, setScrollBarDefaultDelayBeforeFade, setScrollBarFadeDuration, setScrollbarFadingEnabled, setScrollBarSize, setScrollBarStyle, setScrollCaptureCallback, setScrollCaptureHint, setScrollContainer, setScrollIndicators, setScrollIndicators, setScrollX, setScrollY, setSelected, setSoundEffectsEnabled, setStateDescription, setStateListAnimator, setSupplementalDescription, setSystemGestureExclusionRects, setSystemUiVisibility, setTag, setTag, setTextAlignment, setTextDirection, setTooltipText, setTop, setTouchDelegate, setTransitionAlpha, setTransitionName, setTransitionVisibility, setTranslationX, setTranslationY, setTranslationZ, setVerticalFadingEdgeEnabled, setVerticalScrollBarEnabled, setVerticalScrollbarPosition, setVerticalScrollbarThumbDrawable, setVerticalScrollbarTrackDrawable, setViewTranslationCallback, setWillNotCacheDrawing, setWillNotDraw, setX, setY, setZ, showContextMenu, showContextMenu, startActionMode, startActionMode, startAnimation, startDrag, startDragAndDrop, startNestedScroll, stopNestedScroll, toString, transformMatrixToGlobal, transformMatrixToLocal, unscheduleDrawable, unscheduleDrawable, updateDragShadow, verifyDrawable, willNotCacheDrawing, willNotDraw`

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from interface android.view.ViewParent

  `canResolveLayoutDirection, canResolveTextAlignment, canResolveTextDirection, createContextMenu, getLayoutDirection, getParent, getParentForAccessibility, getTextAlignment, getTextDirection, isLayoutDirectionResolved, isLayoutRequested, isTextAlignmentResolved, isTextDirectionResolved, keyboardNavigationClusterSearch, requestFitSystemWindows, requestLayout`

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-init-android-content-Context-com-here-sdk-mapview-MapViewOptions"
    class="section detail">

    ### MapView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapView</span><span class="parameters">(android.content.Context context,
    [MapViewOptions](sdk-for-android-explore-com-here-sdk-mapview-mapviewoptions "class in com.here.sdk.mapview") options)</span>

    </div>

    <div class="block">

    Simple constructor to use when creating a map view from code.

    </div>

    Parameters:  
    `context` - The Context the view is running in, through which it can
    access the current theme, resources, etc.

    `options` - Customization of view for example its map projection.

    </div>

  - <div id="sdk-for-android-explore-init-android-content-Context"
    class="section detail">

    ### MapView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapView</span><span class="parameters">(android.content.Context context)</span>

    </div>

    <div class="block">

    Simple constructor to use when creating a map view from code.

    </div>

    Parameters:  
    `context` - The Context the view is running in, through which it can
    access the current theme, resources, etc.

    </div>

  - <div id="sdk-for-android-explore-init-android-content-Context-android-util-AttributeSet"
    class="section detail">

    ### MapView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapView</span><span class="parameters">(android.content.Context context,
    android.util.AttributeSet attrs)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `context` - The Context the view is running in, through which it can
    access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag
    in an XML document.

    </div>

  - <div id="sdk-for-android-explore-init-android-content-Context-android-util-AttributeSet-int"
    class="section detail">

    ### MapView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapView</span><span class="parameters">(android.content.Context context,
    android.util.AttributeSet attrs, int defStyleAttr)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `context` - The Context the view is running in, through which it can
    access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag
    in an XML document.

    `defStyleAttr` - An attribute in the current theme that contains a
    reference to a style resource that supplies defaults values for the
    StyledAttributes. Can be 0 to not look for defaults.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine-android-content-Context-android-util-AttributeSet-int"
    class="section detail">

    ### MapView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapView</span><span class="parameters">([SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") engine,
    android.content.Context context, android.util.AttributeSet attrs,
    int defStyleAttr)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `engine` - The SDKNativeEngine instance.

    `context` - The Context the view is running in, through which it can
    access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag
    in an XML document..

    `defStyleAttr` - An attribute in the current theme that contains a
    reference to a style resource that supplies defaults values for the
    StyledAttributes. Can be 0 to not look for defaults.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-mapview-MapViewOptions-android-content-Context-android-util-AttributeSet-int"
    class="section detail">

    ### MapView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapView</span><span class="parameters">([SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") engine,
    [MapViewOptions](sdk-for-android-explore-com-here-sdk-mapview-mapviewoptions "class in com.here.sdk.mapview") options,
    android.content.Context context, android.util.AttributeSet attrs,
    int defStyleAttr)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `engine` - The SDKNativeEngine instance.

    `options` - Customization of view for example its map projection.

    `context` - The Context the view is running in, through which it can
    access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag
    in an XML document.

    `defStyleAttr` - An attribute in the current theme that contains a
    reference to a style resource that supplies defaults values for the
    StyledAttributes. Can be 0 to not look for defaults.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-setVisibility-int"
    class="section detail">

    ### setVisibility

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibility</span><span class="parameters">(int visibility)</span>

    </div>

    <div class="block">

    Sets the visibility of MapView. Visibilities of views pinned to
    MapView (see pinView(View, GeoCoordinates) ) will not be affected by
    this method.

    </div>

    Overrides:  
    `setVisibility` in class `android.view.View`

    Parameters:  
    `visibility` - Desired visibility as one of `View.INVISIBLE, View.VISIBLE` or `View.GONE`.

    </div>

  - <div id="sdk-for-android-explore-setPrimaryLanguage-com-here-sdk-core-LanguageCode"
    class="section detail">

    ### setPrimaryLanguage

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setPrimaryLanguage</span><span class="parameters">(@Nullable
    [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode)</span>

    </div>

    <div class="block">

    Set desired primary map display language for all instances of
    MapView. Applying a language change causes map to be redrawn. If
    null is passed or the specified language is not supported, local
    language of the region will be used, which is the default behaviour.

    </div>

    Parameters:  
    `languageCode` - The code of the desired language, or `null` for
    default language.

    </div>

  - <div id="sdk-for-android-explore-setSecondaryLanguage-com-here-sdk-core-LanguageCode"
    class="section detail">

    ### setSecondaryLanguage

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setSecondaryLanguage</span><span class="parameters">(@Nullable
    [LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core") languageCode)</span>

    </div>

    <div class="block">

    Set desired secondary map display language for all instances of
    MapView. Applying a language change causes map to be redrawn. If the
    specified language is not supported, local language of the region
    will be used. If null, no secondary map language will be used which
    is the default behaviour. Note: This feature is in beta state and
    thus there can be bugs and unexpected behavior.

    </div>

    Parameters:  
    `languageCode` - The code of the desired language, or @null to
    unset.

    </div>

  - <div id="sdk-for-android-explore-getPrimaryLanguage"
    class="section detail">

    ### getPrimaryLanguage

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core")</span> <span class="element-name">getPrimaryLanguage</span>()

    </div>

    <div class="block">

    Gets code of currently set primary map display language.

    </div>

    Returns:  
    The code of currently set language or @null language.

    </div>

  - <div id="sdk-for-android-explore-getSecondaryLanguage"
    class="section detail">

    ### getSecondaryLanguage

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core")</span> <span class="element-name">getSecondaryLanguage</span>()

    </div>

    <div class="block">

    Gets code of currently set secondary map display language. Note:
    This feature is in beta state and thus there can be bugs and
    unexpected behavior.

    </div>

    Returns:  
    The code of currently set language or @null language.

    </div>

  - <div id="sdk-for-android-explore-setShadowQuality-com-here-sdk-mapview-ShadowQuality"
    class="section detail">

    ### setShadowQuality

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setShadowQuality</span><span class="parameters">([ShadowQuality](sdk-for-android-explore-com-here-sdk-mapview-shadowquality "enum class in com.here.sdk.mapview") shadowQuality)</span>

    </div>

    <div class="block">

    Set desired shadow quality for all instances of MapView/MapSurface.
    The quality controls the size of the shadow maps and the cascade
    count. The default shadow quality is ShadowQuality.MEDIUM . MapViews
    can request to render shadows by feature. Enabling shadows has a
    performance impact and should be considered only for devices with
    sufficient performance. Note: This feature is in beta state and thus
    there can be bugs and unexpected behavior.

    </div>

    Parameters:  
    `shadowQuality` - The shadow quality.

    </div>

  - <div id="sdk-for-android-explore-getShadowQuality"
    class="section detail">

    ### getShadowQuality

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[ShadowQuality](sdk-for-android-explore-com-here-sdk-mapview-shadowquality "enum class in com.here.sdk.mapview")</span> <span class="element-name">getShadowQuality</span>()

    </div>

    <div class="block">

    Gets the currently set shadow quality. The default shadow quality is
    ShadowQuality.MEDIUM . Note: This feature is in beta state and thus
    there can be bugs and unexpected behavior.

    </div>

    Returns:  
    The currently set shadow quality.

    </div>

  - <div id="sdk-for-android-explore-onCreate-android-os-Bundle"
    class="section detail">

    ### onCreate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onCreate</span><span class="parameters">(android.os.Bundle bundle)</span>

    </div>

    <div class="block">

    Call this method in the onCreate() method of the lifecycle owner
    before calling any other MapView methods. Note: SDKNativeEngine must
    be already initialized before calling this method.

    </div>

    Parameters:  
    `bundle` - The bundle which was passed to onCreate() method of the
    view owner

    </div>

  - <div id="sdk-for-android-explore-onCreate-android-os-Bundle-java-lang-String"
    class="section detail">

    ### onCreate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onCreate</span><span class="parameters">(android.os.Bundle bundle,
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> identifier)</span>

    </div>

    <div class="block">

    Call this method in the onCreate() method of the lifecycle owner
    before calling any other MapView methods if there are multiple
    MapViews instances to (re)create. Note: SDKNativeEngine must be
    already initialized before calling this method.

    </div>

    Parameters:  
    `bundle` - The bundle which was passed to onCreate() method of the
    view owner

    `identifier` - in case of multiple MapView instances use the same
    String which is passed to onSaveInstanceState() to identify each
    MapView.

    </div>

  - <div id="sdk-for-android-explore-setOnReadyListener-com-here-sdk-mapview-MapView-OnReadyListener"
    class="section detail">

    ### setOnReadyListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOnReadyListener</span><span class="parameters">([MapView.OnReadyListener](sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener "interface in com.here.sdk.mapview") readyListener)</span>

    </div>

    <div class="block">

    Sets the OnReadyListener, which will be notified once MapView
    initialization has been finished. It is highly recommended to put
    code that accesses map view related functionality inside
    MapView.OnReadyListener.onMapViewReady() instead of directly in
    Activity 's onResume() .

    </div>

    Parameters:  
    `readyListener` - The listener to be registered, or `null` to
    unregister any previously register listener.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-onResume" class="section detail">

    ### onResume

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onResume</span>()

    </div>

    <div class="block">

    Call this method in the onResume() method of the lifecycle owner.

    </div>

    </div>

  - <div id="sdk-for-android-explore-onPause" class="section detail">

    ### onPause

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onPause</span>()

    </div>

    <div class="block">

    Call this method in the onPause() method of the lifecycle owner.

    </div>

    </div>

  - <div id="sdk-for-android-explore-isValid" class="section detail">

    ### isValid

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValid</span>()

    </div>

    <div class="block">

    Returns whether this MapView is valid. An invalid MapView is
    non-functional. A MapView is considered valid only after
    onCreate(Bundle) or onCreate(Bundle, String) and before onDestroy()
    is called. MapView is also invalidated when the SDKNativeEngine it
    is using is destroyed.

    </div>

    Specified by:  
    [`isValid`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#isValid()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    `true` if this `MapView` is valid, `false` otherwise.

    </div>

  - <div id="sdk-for-android-explore-onDestroy" class="section detail">

    ### onDestroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onDestroy</span>()

    </div>

    <div class="block">

    Call this method in the onDestroy() method of the lifecycle owner

    </div>

    </div>

  - <div id="sdk-for-android-explore-onSaveInstanceState-android-os-Bundle"
    class="section detail">

    ### onSaveInstanceState

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onSaveInstanceState</span><span class="parameters">(android.os.Bundle bundle)</span>

    </div>

    <div class="block">

    Call this method in the onSaveInstance() method of the lifecycle
    owner.

    </div>

    Parameters:  
    `bundle` - the bundle which was passed to lifecycle owner

    </div>

  - <div id="sdk-for-android-explore-onSaveInstanceState-android-os-Bundle-java-lang-String"
    class="section detail">

    ### onSaveInstanceState

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onSaveInstanceState</span><span class="parameters">(android.os.Bundle bundle,
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> identifier)</span>

    </div>

    <div class="block">

    Call this method in the onSaveInstance() method of the lifecycle
    owner if multiple MapView instances are present. Each MapView
    instance should have its own identifier string which is passed to
    onSaveInstanceState() and onCreate() methods.

    </div>

    Parameters:  
    `bundle` - The bundle which was passed to lifecycle owner.

    `identifier` - If multiple MapView instances are under the same
    lifecycle owner then provide a unique string to identify each
    MapView instance.

    </div>

  - <div id="sdk-for-android-explore-pick-com-here-sdk-mapview-MapScene-MapPickFilter-com-here-sdk-core-Rectangle2D-com-here-sdk-mapview-MapViewBase-MapPickCallback"
    class="section detail">

    ### pick

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">pick</span><span class="parameters">(@Nullable
    [MapScene.MapPickFilter](sdk-for-android-explore-com-here-sdk-mapview-mapscene-mappickfilter "class in com.here.sdk.mapview") filter,
    @NonNull
    [Rectangle2D](sdk-for-android-explore-com-here-sdk-core-rectangle2d "class in com.here.sdk.core") viewArea,
    @NonNull
    [MapViewBase.MapPickCallback](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase-mappickcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Returns all map content located inside the specified pick area.
    Content to be picked is specified by a pick content filter. The pick
    area is defined by a rectangle in map view coordinates in pixels,
    relative to the map view's origin at (0, 0) which indicates the
    top-left corner of the map view.

    </div>

    Specified by:  
    [`pick`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `filter` -

    Filter for the map content to be picked. When a filter is not set
    all of the pickable content will be picked.

    `viewArea` -

    The rectangular pixel area of the view inside which map content will
    be picked. View area is relative to the map view's origin at (0, 0)
    at the top-left corner of the map view.

    `callback` -

    Callback to call with the result. This will be called on a main
    thread when pick operation completes.

    </div>

  - <div id="sdk-for-android-explore-geoToViewCoordinates-com-here-sdk-core-GeoCoordinates"
    class="section detail">

    ### geoToViewCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")</span> <span class="element-name">geoToViewCoordinates</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") geoCoordinates)</span>

    </div>

    <div class="block">

    Converts geographical coordinates to view coordinates (in pixels).
    If specified, altitude of the input coordinates is interpreted as
    altitude above sea level. If not specified, the input coordinates
    are interpreted as being on ground elevation. The above distinction
    is only relevant when 3D terrain feature is enabled. The resulting
    view coordinates might be outside of current viewport, i.e. result
    might contain values less than zero or greater than view's
    dimensions. If the render surface is not attached, it will return
    null .

    </div>

    Specified by:  
    [`geoToViewCoordinates`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `geoCoordinates` -

    Geographical coordinates to convert.

    Returns:  
    The view coordinates of the specified geographical point or `null`
    if there is no render surface attached.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    See Also:  
    - [`MapView.OnReadyListener`](sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener "interface in com.here.sdk.mapview")

    </div>

  - <div id="sdk-for-android-explore-addLifecycleListener-com-here-sdk-mapview-MapViewLifecycleListener"
    class="section detail">

    ### addLifecycleListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLifecycleListener</span><span class="parameters">(@NonNull
    [MapViewLifecycleListener](sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)</span>

    </div>

    <div class="block">

    Adds a MapViewLifecycleListener to this map view. Adding the same
    object multiple times has no effect.

    </div>

    Specified by:  
    [`addLifecycleListener`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `lifecycleListener` - An object to be notified of lifecycle events.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-removeLifecycleListener-com-here-sdk-mapview-MapViewLifecycleListener"
    class="section detail">

    ### removeLifecycleListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLifecycleListener</span><span class="parameters">(@NonNull
    [MapViewLifecycleListener](sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)</span>

    </div>

    <div class="block">

    Removes a MapViewLifecycleListener from this map view. Trying to
    remove an object that was not added or was removed before has no
    effect.

    </div>

    Specified by:  
    [`removeLifecycleListener`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `lifecycleListener` - An object to stop being notified of lifecycle
    events.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-pinView-android-view-View-com-here-sdk-core-GeoCoordinates"
    class="section detail">

    ### pinView

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[MapView.ViewPin](sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin "interface in com.here.sdk.mapview")</span> <span class="element-name">pinView</span><span class="parameters">(@NonNull
    android.view.View view,
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Pins a View to the MapView and returns a proxy object that can be
    used to control the pinning. Trying to pin a view that was already
    pinned or a view that has a parent has no effect and returns null .
    The altitude component of the coordinates, if set, is interpreted as
    above sea level. When not set, the coordinates are interpreted as at
    ground level.

    </div>

    Parameters:  
    `view` - `View` to add.

    `coordinates` - `GeoCoordinates` to pin the view at.

    Returns:  
    The handle to a pinned view, or `null` if the view could not be
    pinned to the map.

    </div>

  - <div id="sdk-for-android-explore-unpinView-android-view-View"
    class="section detail">

    ### unpinView

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unpinView</span><span class="parameters">(@NonNull
    android.view.View view)</span>

    </div>

    <div class="block">

    Removes a MapView.ViewPin from the MapView by specifying the
    corresponding view. Trying to unpin a view that was not pinned or
    was unpinned before has no effect.

    </div>

    Parameters:  
    `view` - The view corresponding to the `ViewPin` to remove.

    </div>

  - <div id="sdk-for-android-explore-getViewPins"
    class="section detail">

    ### getViewPins

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[MapView.ViewPin](sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin "interface in com.here.sdk.mapview")\></span> <span class="element-name">getViewPins</span>()

    </div>

    <div class="block">

    Returns a copy of the list of views currently pinned to the map
    view.

    </div>

    Returns:  
    A copy of the list of view pins.

    </div>

  - <div id="sdk-for-android-explore-viewToGeoCoordinates-com-here-sdk-core-Point2D"
    class="section detail">

    ### viewToGeoCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">viewToGeoCoordinates</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") viewCoordinates)</span>

    </div>

    <div class="block">

    Converts view coordinates to geographical coordinates. An optional
    altitude component of the resulting geographical coordinate is not
    set. If the view coordinates specify a point above a horizon, then
    the result is geographical coordinates of the point on a horizon
    below the specified view coordinates. The fog effect is ignored for
    the calculation, meaning that for the view point within the area
    covered by the fog, the result is geographical coordinates that
    would be displayed at the specified point if the fog effect was not
    applied. If the render surface is not attached, it will return null
    .

    </div>

    Specified by:  
    [`viewToGeoCoordinates`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#viewToGeoCoordinates(com.here.sdk.core.Point2D)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `viewCoordinates` -

    Point inside the view to convert.

    Returns:  
    The geographical coordinates under specified view point or `null` if
    there is no render surface attached.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    See Also:  
    - [`MapView.OnReadyListener`](sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener "interface in com.here.sdk.mapview")

    </div>

  - <div id="sdk-for-android-explore-getGestures"
    class="section detail">

    ### getGestures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Gestures](sdk-for-android-explore-com-here-sdk-gestures-gestures "class in com.here.sdk.gestures")</span> <span class="element-name">getGestures</span>()

    </div>

    <div class="block">

    Returns the gestures control object

    </div>

    Specified by:  
    [`getGestures`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getGestures()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    the
    [`Gestures`](sdk-for-android-explore-com-here-sdk-gestures-gestures "class in com.here.sdk.gestures")
    control object

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-getPixelScale"
    class="section detail">

    ### getPixelScale

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPixelScale</span>()

    </div>

    <div class="block">

    Gets the pixel scale factor used by this MapView. It is is used to
    support screen resolution and size independence. This value is a
    derivative of the device's screen pixel density and is a direct
    analog of pixel density from DisplayMetrics. It can be used to
    translate between physical pixels and density independent pixels
    according to formula: dp = px / pixel_scale

    </div>

    Specified by:  
    [`getPixelScale`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getPixelScale()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    current pixel scale factor, or 0.0 if MapView is not initialized

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-getViewportSize"
    class="section detail">

    ### getViewportSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">[Size2D](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")</span> <span class="element-name">getViewportSize</span>()

    </div>

    <div class="block">

    Gets the size of this map view in physical pixels. If internally the
    map view's render surface is not attached yet (see:
    MapViewLifecycleListener ), or after the map view has been destroyed
    then a Size2D with zero width and height is returned.

    </div>

    Specified by:  
    [`getViewportSize`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getViewportSize()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    The viewport size in physical pixels, or Size2D(0.0,0.0) if MapView
    is not initialized

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-getFrameRate"
    class="section detail">

    ### getFrameRate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getFrameRate</span>()

    </div>

    <div class="block">

    Gets maximum render frame rate in frames per second. The default
    value is 60 frames per second.

    </div>

    Specified by:  
    [`getFrameRate`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getFrameRate()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    Actual maximal render frame rate

    </div>

  - <div id="sdk-for-android-explore-setFrameRate-int"
    class="section detail">

    ### setFrameRate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFrameRate</span><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets maximum render frame rate in frames per second.

    </div>

    Specified by:  
    [`setFrameRate`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#setFrameRate(int)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `value` - Maximum render frame rate in frames per second. Setting to
    0 disables automatic rendering for this view. Setting negative
    values has no effect.

    </div>

  - <div id="sdk-for-android-explore-takeScreenshot-com-here-sdk-mapview-MapView-TakeScreenshotCallback"
    class="section detail">

    ### takeScreenshot

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">takeScreenshot</span><span class="parameters">([MapView.TakeScreenshotCallback](sdk-for-android-explore-com-here-sdk-mapview-mapview-takescreenshotcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Asynchronously retrieves a screenshot of current map view. Note that
    this may not work when the map view is currently not visible, for
    example, when an application is running in background and onPause()
    was called.

    </div>

    Parameters:  
    `callback` - Completion handler called when the screenshot is
    completed

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-setWatermarkLocation-com-here-sdk-core-Anchor2D-com-here-sdk-core-Point2D"
    class="section detail">

    ### setWatermarkLocation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWatermarkLocation</span><span class="parameters">(@NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") anchor,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") offset)</span>

    </div>

    <div class="block">

    Sets the position of the HERE logo watermark within the map view. By
    default, the watermark is aligned to the bottom-right corner of the
    view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2,
    -watermarkSize.height / 2). It is recommended to change the default
    position only if necessary to avoid overlapping UI elements. The
    watermark should always be fully visible within the view. The anchor
    point on the watermark is its center (width/2, height/2), around
    which it will be placed in the map view. For map views smaller than
    250 dip in both width and height, the watermark will not be shown.

    </div>

    Specified by:  
    [`setWatermarkLocation`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Parameters:  
    `anchor` -

    Anchor point in normalized view coordinates \[0, 1\]. Map view's
    origin at (0, 0) indicates a top-left corner of the map view. Out of
    boundary anchor point values will be clamped to the \[0, 1\] range.

    `offset` -

    A horizontal and vertical offset (expressed in positive/negative
    pixel coordinates) that allows shifting the watermark from the
    anchor point position in one or the other direction. For the
    quadrant of values expressing visible part of the map view negative
    offset shifts the watermark to the direction of the origin,
    positive - away from it. For example, the offset of (-10, 5) will
    shift the watermark 10px to the left and 5px to the bottom. If
    specified offset will result in watermark being completely or
    partially out-of-view the offset will be adjusted internally so that
    watermark is fully visible. Offset is not being scaled when the map
    view size changes.

    </div>

  - <div id="sdk-for-android-explore-getWatermarkSize"
    class="section detail">

    ### getWatermarkSize

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Size2D](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")</span> <span class="element-name">getWatermarkSize</span>()

    </div>

    <div class="block">

    Returns the watermark size in physical pixels.

    </div>

    Specified by:  
    [`getWatermarkSize`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getWatermarkSize()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    Provides the size of the watermark in physical pixels.

    </div>

  - <div id="sdk-for-android-explore-getCamera" class="section detail">

    ### getCamera

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapCamera](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")</span> <span class="element-name">getCamera</span>()

    </div>

    <div class="block">

    Gets the camera control object for the map.

    </div>

    Specified by:  
    [`getCamera`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getCamera()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    the
    [`MapCamera`](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")
    object for the map.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-getMapScene"
    class="section detail">

    ### getMapScene

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapScene](sdk-for-android-explore-com-here-sdk-mapview-mapscene "class in com.here.sdk.mapview")</span> <span class="element-name">getMapScene</span>()

    </div>

    <div class="block">

    Gets the map scene associated with this map view. This can be used
    to request different map schemes to be displayed in the map view,
    and to add and remove map items from the map.

    </div>

    Specified by:  
    [`getMapScene`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getMapScene()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    the
    [`MapScene`](sdk-for-android-explore-com-here-sdk-mapview-mapscene "class in com.here.sdk.mapview")
    associated with this map view.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-getMapContext"
    class="section detail">

    ### getMapContext

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")</span> <span class="element-name">getMapContext</span>()

    </div>

    <div class="block">

    Gets the map context associated with this map view.

    </div>

    Specified by:  
    [`getMapContext`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getMapContext()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    the
    [`MapContext`](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")
    associated with this map view.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-getHereMap" class="section detail">

    ### getHereMap

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[HereMap](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview")</span> <span class="element-name">getHereMap</span>()

    </div>

    <div class="block">

    Gets the HereMap associated with this map view.

    </div>

    Specified by:  
    [`getHereMap`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getHereMap()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    the
    [`HereMap`](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview")
    associated with this map view.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if
    [](sdk-for-android-explore-com-here-sdk-mapview-mapview#onCreate(android.os.Bundle))

        onCreate(Bundle)

    method was not called beforehand.

    </div>

  - <div id="sdk-for-android-explore-setFixedSize-int-int-double"
    class="section detail">

    ### setFixedSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFixedSize</span><span class="parameters">(int width,
    int height, double factor)</span>

    </div>

    <div class="block">

    Requests a fixed size to be used for rendering this MapView. Use
    this feature to render MapView to a smaller size and let the system
    upscale to actual on-screen size. The new fixed size is expected to
    have the same aspect ratio as the on-screen size and the factor
    provided to match the factor applied to the on-screen size that
    leads to the new fixed size: - width = on-screen width \* factor -
    height = on-screen height \* factor Note: This feature is in beta
    state and thus there can be bugs and unexpected behavior.

    </div>

    Parameters:  
    `width` - Fixed width to be used, in pixels.

    `height` - Fixed height to be used, in pixels.

    `factor` - Factor in between (0.0, 1.0\] by which screen size
    differs from fixed size.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if factor is not inside (0.0, 1.0\].

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html"
    class="external-link"
    title="class or interface in java.lang"><code>UnsupportedOperationException</code></a> -
    if
    [`MapView`](sdk-for-android-explore-com-here-sdk-mapview-mapview "class in com.here.sdk.mapview")
    render mode is not MapRenderMode.SURFACE.

    </div>

  </div>

