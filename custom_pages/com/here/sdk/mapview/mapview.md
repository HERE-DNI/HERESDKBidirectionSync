---
title: "MapView (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapview"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapView

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
android.view.View
android.view.ViewGroup
android.widget.FrameLayout
com.here.sdk.mapview.MapView
All Implemented Interfaces:
`android.graphics.drawable.Drawable.Callback`, `android.view.accessibility.AccessibilityEventSource`, `android.view.KeyEvent.Callback`, `android.view.ViewManager`, `android.view.ViewParent`, [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

------------------------------------------------------------------------
public class MapView extends android.widget.FrameLayout implements [MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")
A view that can display a map.

The content of the map is controlled by [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview"), which is accessible by calling [`getMapScene()`](#getMapScene()). To display a map, map scene needs to be loaded with [`MapScene.loadScene(MapScheme, MapScene.LoadSceneCallback)`](sdk-for-android-explore-api-reference-latestmapscene#loadScene(com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.MapScene.LoadSceneCallback)).

Manipulating the way the map is displayed is possible using [`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview"), which is accessible by calling [`getCamera()`](#getCamera()).

Gesture handling can be modified through the [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") object, which is accessible by calling [`getGestures()`](#getGestures()).

## Permissions

To use the MapView the following application permissions need to be present: android.permission.INTERNET and android.permission.ACCESS_NETWORK_STATE

## Rendering mode

`MapView` can draw the map using either `SurfaceView` or `TextureView`.

`SurfaceView` is the default method, offers best performance and works best for single screen applications where there's a single `MapView` which is not part of a complex view hierarchy and takes no part in any UI animations. This method is known to cause graphical glitches in some scenarios (like embedding multiple `MapView`s inside a view pager), especially on Android 12 and newer.

`TextureView` is less performant, but behaves like any other view and can be easily transformed and animated, making it a better fit for applications with complex UI and/or multiple `MapView`s as part of a complex view hierarchy.

Rendering mode can only be set when creating a `MapView`, by setting [`MapViewOptions.renderMode`](sdk-for-android-explore-api-reference-latestmapviewoptions#renderMode) and passing the options to the constructor.

## Coordinate systems

When dealing with view coordinates, physical pixels are used. MapView provides ways to translate between view and geographic coordinates using [`viewToGeoCoordinates(Point2D)`](#viewToGeoCoordinates(com.here.sdk.core.Point2D)) and [`geoToViewCoordinates(GeoCoordinates)`](#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)) methods. Note that those two methods only work when the MapView is fully ready, so if there is a need to call them during lifecycle changes, they should be called from within [`MapView.OnReadyListener.onMapViewReady()`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener#onMapViewReady()). See Lifecycle section below for more details.

## Map caching

Two caching mechanisms are supported. First is in-memory cache, which keeps some number of map tiles around in memory to avoid repeated network requests or storage reads. The second mechanism is persistent cache that stores downloaded map data on the device. Persistent cache requires storage permission to be granted.

## Lifecycle

For `MapView` to work correctly, it is required to call its lifecycle methods from the owner Activity: [`onCreate(Bundle)`](#onCreate(android.os.Bundle)), [`onResume()`](#onResume()), [`onPause()`](#onPause()), [`onDestroy()`](#onDestroy()) and [`onSaveInstanceState(Bundle)`](#onSaveInstanceState(android.os.Bundle)).

When dealing with multiple `MapView`s in a single Activity, an extra identifier needs to be passed to [`onCreate(Bundle, String)`](#onCreate(android.os.Bundle,java.lang.String)) and [`onSaveInstanceState(Bundle, String)`](#onSaveInstanceState(android.os.Bundle,java.lang.String)). This identifier needs to be unique to all the `MapView`s owned by the `Activity` and needs to be the same when recreating the `Activity`.

A `MapView` is considered valid only after [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) or [`onCreate(Bundle, String)`](#onCreate(android.os.Bundle,java.lang.String)) and before [`onDestroy()`](#onDestroy()) is called. `MapView` is also invalidated when the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") it is using is destroyed. [`isValid()`](#isValid()) can be used to check the state of `MapView`.

`MapView` offers additional lifecycle event exposed through [`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview"). This can be used to determine when `MapView` is fully ready for action, which means that map scene is loaded and drawing surface is ready to render a map. This is important for coordinate conversion methods and [`getViewportSize()`](#getViewportSize()), which work only when those conditions are met. When `OnReadyListener` is set in `Activity`'s `onCreate()` before any other operation is performed on the `MapView`, then [`MapView.OnReadyListener.onMapViewReady()`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener#onMapViewReady()) is called:

- after map scene is successfully loaded for the first time
- some time after `Activity`'s `onResume()`, assuming map scene had been loaded before

Note: Before using any API in this class, `SDKNativeEngine` must be already initialized.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [MapView.OnReadyListener](sdk-for-android-explore-api-reference-latestmapview-onreadylistener)

Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map.

`static interface `

  [MapView.TakeScreenshotCallback](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback)

Callback to be called on retrieval of screenshot.

`static interface `

  [MapView.ViewPin](sdk-for-android-explore-api-reference-latestmapview-viewpin)

A ViewPin is used to display Android views at a fixed location on the map.

## Nested classes/interfaces inherited from class android.widget.FrameLayout

  `android.widget.FrameLayout.LayoutParams`

## Nested classes/interfaces inherited from class android.view.ViewGroup

  `android.view.ViewGroup.MarginLayoutParams, android.view.ViewGroup.OnHierarchyChangeListener`

## Nested classes/interfaces inherited from class android.view.View

  `android.view.View.AccessibilityDelegate, android.view.View.BaseSavedState, android.view.View.DragShadowBuilder, android.view.View.MeasureSpec, android.view.View.OnApplyWindowInsetsListener, android.view.View.OnAttachStateChangeListener, android.view.View.OnCapturedPointerListener, android.view.View.OnClickListener, android.view.View.OnContextClickListener, android.view.View.OnCreateContextMenuListener, android.view.View.OnDragListener, android.view.View.OnFocusChangeListener, android.view.View.OnGenericMotionListener, android.view.View.OnHoverListener, android.view.View.OnKeyListener, android.view.View.OnLayoutChangeListener, android.view.View.OnLongClickListener, android.view.View.OnScrollChangeListener, android.view.View.OnSystemUiVisibilityChangeListener, android.view.View.OnTouchListener, android.view.View.OnUnhandledKeyEventListener`

## Nested classes/interfaces inherited from interface com.here.sdk.mapview.[MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

  [`MapViewBase.MapPickCallback`](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")

## Field Summary

### Fields inherited from class android.view.ViewGroup

  `CLIP_TO_PADDING_MASK, FOCUS_AFTER_DESCENDANTS, FOCUS_BEFORE_DESCENDANTS, FOCUS_BLOCK_DESCENDANTS, LAYOUT_MODE_CLIP_BOUNDS, LAYOUT_MODE_OPTICAL_BOUNDS, PERSISTENT_ALL_CACHES, PERSISTENT_ANIMATION_CACHE, PERSISTENT_NO_CACHE, PERSISTENT_SCROLLING_CACHE`

### Fields inherited from class android.view.View

  `ACCESSIBILITY_DATA_SENSITIVE_AUTO, ACCESSIBILITY_DATA_SENSITIVE_NO, ACCESSIBILITY_DATA_SENSITIVE_YES, ACCESSIBILITY_LIVE_REGION_ASSERTIVE, ACCESSIBILITY_LIVE_REGION_NONE, ACCESSIBILITY_LIVE_REGION_POLITE, ALPHA, AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH, AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR, AUTOFILL_HINT_CREDIT_CARD_NUMBER, AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE, AUTOFILL_HINT_EMAIL_ADDRESS, AUTOFILL_HINT_NAME, AUTOFILL_HINT_PASSWORD, AUTOFILL_HINT_PHONE, AUTOFILL_HINT_POSTAL_ADDRESS, AUTOFILL_HINT_POSTAL_CODE, AUTOFILL_HINT_USERNAME, AUTOFILL_TYPE_DATE, AUTOFILL_TYPE_LIST, AUTOFILL_TYPE_NONE, AUTOFILL_TYPE_TEXT, AUTOFILL_TYPE_TOGGLE, CONTENT_SENSITIVITY_AUTO, CONTENT_SENSITIVITY_NOT_SENSITIVE, CONTENT_SENSITIVITY_SENSITIVE, DRAG_FLAG_ACCESSIBILITY_ACTION, DRAG_FLAG_GLOBAL, DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION, DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION, DRAG_FLAG_GLOBAL_SAME_APPLICATION, DRAG_FLAG_GLOBAL_URI_READ, DRAG_FLAG_GLOBAL_URI_WRITE, DRAG_FLAG_OPAQUE, DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG, DRAWING_CACHE_QUALITY_AUTO, DRAWING_CACHE_QUALITY_HIGH, DRAWING_CACHE_QUALITY_LOW, EMPTY_STATE_SET, ENABLED_FOCUSED_SELECTED_STATE_SET, ENABLED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, ENABLED_FOCUSED_STATE_SET, ENABLED_FOCUSED_WINDOW_FOCUSED_STATE_SET, ENABLED_SELECTED_STATE_SET, ENABLED_SELECTED_WINDOW_FOCUSED_STATE_SET, ENABLED_STATE_SET, ENABLED_WINDOW_FOCUSED_STATE_SET, FIND_VIEWS_WITH_CONTENT_DESCRIPTION, FIND_VIEWS_WITH_TEXT, FOCUS_BACKWARD, FOCUS_DOWN, FOCUS_FORWARD, FOCUS_LEFT, FOCUS_RIGHT, FOCUS_UP, FOCUSABLE, FOCUSABLE_AUTO, FOCUSABLES_ALL, FOCUSABLES_TOUCH_MODE, FOCUSED_SELECTED_STATE_SET, FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, FOCUSED_STATE_SET, FOCUSED_WINDOW_FOCUSED_STATE_SET, GONE, HAPTIC_FEEDBACK_ENABLED, IMPORTANT_FOR_ACCESSIBILITY_AUTO, IMPORTANT_FOR_ACCESSIBILITY_NO, IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS, IMPORTANT_FOR_ACCESSIBILITY_YES, IMPORTANT_FOR_AUTOFILL_AUTO, IMPORTANT_FOR_AUTOFILL_NO, IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_AUTOFILL_YES, IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_CONTENT_CAPTURE_AUTO, IMPORTANT_FOR_CONTENT_CAPTURE_NO, IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS, IMPORTANT_FOR_CONTENT_CAPTURE_YES, IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS, INVISIBLE, KEEP_SCREEN_ON, LAYER_TYPE_HARDWARE, LAYER_TYPE_NONE, LAYER_TYPE_SOFTWARE, LAYOUT_DIRECTION_INHERIT, LAYOUT_DIRECTION_LOCALE, LAYOUT_DIRECTION_LTR, LAYOUT_DIRECTION_RTL, MEASURED_HEIGHT_STATE_SHIFT, MEASURED_SIZE_MASK, MEASURED_STATE_MASK, MEASURED_STATE_TOO_SMALL, NO_ID, NOT_FOCUSABLE, OVER_SCROLL_ALWAYS, OVER_SCROLL_IF_CONTENT_SCROLLS, OVER_SCROLL_NEVER, PRESSED_ENABLED_FOCUSED_SELECTED_STATE_SET, PRESSED_ENABLED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_FOCUSED_STATE_SET, PRESSED_ENABLED_FOCUSED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_SELECTED_STATE_SET, PRESSED_ENABLED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_ENABLED_STATE_SET, PRESSED_ENABLED_WINDOW_FOCUSED_STATE_SET, PRESSED_FOCUSED_SELECTED_STATE_SET, PRESSED_FOCUSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_FOCUSED_STATE_SET, PRESSED_FOCUSED_WINDOW_FOCUSED_STATE_SET, PRESSED_SELECTED_STATE_SET, PRESSED_SELECTED_WINDOW_FOCUSED_STATE_SET, PRESSED_STATE_SET, PRESSED_WINDOW_FOCUSED_STATE_SET, REQUESTED_FRAME_RATE_CATEGORY_DEFAULT, REQUESTED_FRAME_RATE_CATEGORY_HIGH, REQUESTED_FRAME_RATE_CATEGORY_LOW, REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE, REQUESTED_FRAME_RATE_CATEGORY_NORMAL, ROTATION, ROTATION_X, ROTATION_Y, SCALE_X, SCALE_Y, SCREEN_STATE_OFF, SCREEN_STATE_ON, SCROLL_AXIS_HORIZONTAL, SCROLL_AXIS_NONE, SCROLL_AXIS_VERTICAL, SCROLL_CAPTURE_HINT_AUTO, SCROLL_CAPTURE_HINT_EXCLUDE, SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS, SCROLL_CAPTURE_HINT_INCLUDE, SCROLL_INDICATOR_BOTTOM, SCROLL_INDICATOR_END, SCROLL_INDICATOR_LEFT, SCROLL_INDICATOR_RIGHT, SCROLL_INDICATOR_START, SCROLL_INDICATOR_TOP, SCROLLBAR_POSITION_DEFAULT, SCROLLBAR_POSITION_LEFT, SCROLLBAR_POSITION_RIGHT, SCROLLBARS_INSIDE_INSET, SCROLLBARS_INSIDE_OVERLAY, SCROLLBARS_OUTSIDE_INSET, SCROLLBARS_OUTSIDE_OVERLAY, SELECTED_STATE_SET, SELECTED_WINDOW_FOCUSED_STATE_SET, SOUND_EFFECTS_ENABLED, STATUS_BAR_HIDDEN, STATUS_BAR_VISIBLE, SYSTEM_UI_FLAG_FULLSCREEN, SYSTEM_UI_FLAG_HIDE_NAVIGATION, SYSTEM_UI_FLAG_IMMERSIVE, SYSTEM_UI_FLAG_IMMERSIVE_STICKY, SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN, SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION, SYSTEM_UI_FLAG_LAYOUT_STABLE, SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR, SYSTEM_UI_FLAG_LIGHT_STATUS_BAR, SYSTEM_UI_FLAG_LOW_PROFILE, SYSTEM_UI_FLAG_VISIBLE, SYSTEM_UI_LAYOUT_FLAGS, TEXT_ALIGNMENT_CENTER, TEXT_ALIGNMENT_GRAVITY, TEXT_ALIGNMENT_INHERIT, TEXT_ALIGNMENT_TEXT_END, TEXT_ALIGNMENT_TEXT_START, TEXT_ALIGNMENT_VIEW_END, TEXT_ALIGNMENT_VIEW_START, TEXT_DIRECTION_ANY_RTL, TEXT_DIRECTION_FIRST_STRONG, TEXT_DIRECTION_FIRST_STRONG_LTR, TEXT_DIRECTION_FIRST_STRONG_RTL, TEXT_DIRECTION_INHERIT, TEXT_DIRECTION_LOCALE, TEXT_DIRECTION_LTR, TEXT_DIRECTION_RTL, TRANSLATION_X, TRANSLATION_Y, TRANSLATION_Z, VIEW_LOG_TAG, VISIBLE, WINDOW_FOCUSED_STATE_SET, X, Y, Z`

## Constructor Summary

Constructors

Constructor

  Description

  [MapView](#%3Cinit%3E(android.content.Context))`(android.content.Context context)`

Simple constructor to use when creating a map view from code.

[MapView](#%3Cinit%3E(android.content.Context,android.util.AttributeSet))`(android.content.Context context, android.util.AttributeSet attrs)`

Creates a new instance.

[MapView](#%3Cinit%3E(android.content.Context,android.util.AttributeSet,int))`(android.content.Context context, android.util.AttributeSet attrs, int defStyleAttr)`

Creates a new instance.

[MapView](#%3Cinit%3E(android.content.Context,com.here.sdk.mapview.MapViewOptions))`(android.content.Context context, `[`MapViewOptions`](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview")` options)`

Simple constructor to use when creating a map view from code.

[MapView](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,android.content.Context,android.util.AttributeSet,int))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` engine, android.content.Context context, android.util.AttributeSet attrs, int defStyleAttr)`

Creates a new instance.

[MapView](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapview.MapViewOptions,android.content.Context,android.util.AttributeSet,int))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` engine, `[`MapViewOptions`](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview")` options, android.content.Context context, android.util.AttributeSet attrs, int defStyleAttr)`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [addLifecycleListener](#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener))`(`[`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")` lifecycleListener)`

Adds a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to this map view.

[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

  [geoToViewCoordinates](#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoCoordinates)`

Converts geographical coordinates to view coordinates (in pixels).

[`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")

  [getCamera](#getCamera())`()`

Gets the camera control object for the map.

`int`

  [getFrameRate](#getFrameRate())`()`

Gets maximum render frame rate in frames per second.

[`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures")

  [getGestures](#getGestures())`()`

Returns the gestures control object

[`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")

  [getHereMap](#getHereMap())`()`

Gets the HereMap associated with this map view.

[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")

  [getMapContext](#getMapContext())`()`

Gets the map context associated with this map view.

[`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")

  [getMapScene](#getMapScene())`()`

Gets the map scene associated with this map view.

`double`

  [getPixelScale](#getPixelScale())`()`

Gets the pixel scale factor used by this MapView.

`static `[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

  [getPrimaryLanguage](#getPrimaryLanguage())`()`

Gets code of currently set primary map display language.

`static `[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

  [getSecondaryLanguage](#getSecondaryLanguage())`()`

Gets code of currently set secondary map display language.

`static `[`ShadowQuality`](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview")

  [getShadowQuality](#getShadowQuality())`()`

Gets the currently set shadow quality.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapView.ViewPin`](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview")`>`

  [getViewPins](#getViewPins())`()`

Returns a copy of the list of views currently pinned to the map view.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [getViewportSize](#getViewportSize())`()`

Gets the size of this map view in physical pixels.

[`Size2D`](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

  [getWatermarkSize](#getWatermarkSize())`()`

Returns the watermark size in physical pixels.

`boolean`

  [isValid](#isValid())`()`

Returns whether this `MapView` is valid.

`void`

  [onCreate](#onCreate(android.os.Bundle))`(android.os.Bundle bundle)`

Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods.

`void`

  [onCreate](#onCreate(android.os.Bundle,java.lang.String))`(android.os.Bundle bundle, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` identifier)`

Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods if there are multiple MapViews instances to (re)create.

`void`

  [onDestroy](#onDestroy())`()`

Call this method in the onDestroy() method of the lifecycle owner

`void`

  [onPause](#onPause())`()`

Call this method in the onPause() method of the lifecycle owner.

`void`

  [onResume](#onResume())`()`

Call this method in the onResume() method of the lifecycle owner.

`void`

  [onSaveInstanceState](#onSaveInstanceState(android.os.Bundle))`(android.os.Bundle bundle)`

Call this method in the onSaveInstance() method of the lifecycle owner.

`void`

  [onSaveInstanceState](#onSaveInstanceState(android.os.Bundle,java.lang.String))`(android.os.Bundle bundle, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` identifier)`

Call this method in the onSaveInstance() method of the lifecycle owner if multiple MapView instances are present.

`void`

  [pick](#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback))`(`[`MapScene.MapPickFilter`](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview")` filter, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewArea, `[`MapViewBase.MapPickCallback`](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")` callback)`

Returns all map content located inside the specified pick area.

[`MapView.ViewPin`](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview")

  [pinView](#pinView(android.view.View,com.here.sdk.core.GeoCoordinates))`(android.view.View view, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates)`

Pins a `View` to the `MapView` and returns a proxy object that can be used to control the pinning.

`void`

  [removeLifecycleListener](#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener))`(`[`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")` lifecycleListener)`

Removes a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from this map view.

`void`

  [setFixedSize](#setFixedSize(int,int,double))`(int width, int height, double factor)`

Requests a fixed size to be used for rendering this MapView.

`void`

  [setFrameRate](#setFrameRate(int))`(int value)`

Sets maximum render frame rate in frames per second.

`void`

  [setOnReadyListener](#setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener))`(`[`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")` readyListener)`

Sets the OnReadyListener, which will be notified once MapView initialization has been finished.

`static void`

  [setPrimaryLanguage](#setPrimaryLanguage(com.here.sdk.core.LanguageCode))`(`[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")` languageCode)`

Set desired primary map display language for all instances of MapView.

`static void`

  [setSecondaryLanguage](#setSecondaryLanguage(com.here.sdk.core.LanguageCode))`(`[`LanguageCode`](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")` languageCode)`

Set desired secondary map display language for all instances of MapView.

`static void`

  [setShadowQuality](#setShadowQuality(com.here.sdk.mapview.ShadowQuality))`(`[`ShadowQuality`](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview")` shadowQuality)`

Set desired shadow quality for all instances of MapView/MapSurface.

`void`

  [setVisibility](#setVisibility(int))`(int visibility)`

Sets the visibility of MapView.

`void`

  [setWatermarkLocation](#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchor, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` offset)`

Sets the position of the HERE logo watermark within the map view.

`void`

  [takeScreenshot](#takeScreenshot(com.here.sdk.mapview.MapView.TakeScreenshotCallback))`(`[`MapView.TakeScreenshotCallback`](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback "interface in com.here.sdk.mapview")` callback)`

Asynchronously retrieves a screenshot of current map view.

`void`

  [unpinView](#unpinView(android.view.View))`(android.view.View view)`

Removes a [`MapView.ViewPin`](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview") from the `MapView` by specifying the corresponding view.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [viewToGeoCoordinates](#viewToGeoCoordinates(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewCoordinates)`

Converts view coordinates to geographical coordinates.

### Methods inherited from class android.widget.FrameLayout

  `checkLayoutParams, generateDefaultLayoutParams, generateLayoutParams, generateLayoutParams, getAccessibilityClassName, getConsiderGoneChildrenWhenMeasuring, getMeasureAllChildren, onLayout, onMeasure, setForegroundGravity, setMeasureAllChildren, shouldDelayChildPressedState`

### Methods inherited from class android.view.ViewGroup

  `addChildrenForAccessibility, addExtraDataToAccessibilityNodeInfo, addFocusables, addKeyboardNavigationClusters, addStatesFromChildren, addTouchables, addView, addView, addView, addView, addView, addViewInLayout, addViewInLayout, attachLayoutAnimationParameters, attachViewToParent, bringChildToFront, canAnimate, childDrawableStateChanged, childHasTransientStateChanged, cleanupLayoutState, clearChildFocus, clearDisappearingChildren, clearFocus, debug, detachAllViewsFromParent, detachViewFromParent, detachViewFromParent, detachViewsFromParent, dispatchApplyWindowInsets, dispatchCapturedPointerEvent, dispatchConfigurationChanged, dispatchCreateViewTranslationRequest, dispatchDisplayHint, dispatchDragEvent, dispatchDraw, dispatchDrawableHotspotChanged, dispatchFinishTemporaryDetach, dispatchFreezeSelfOnly, dispatchGenericFocusedEvent, dispatchGenericPointerEvent, dispatchHoverEvent, dispatchKeyEvent, dispatchKeyEventPreIme, dispatchKeyShortcutEvent, dispatchPointerCaptureChanged, dispatchProvideAutofillStructure, dispatchProvideStructure, dispatchRestoreInstanceState, dispatchSaveInstanceState, dispatchScrollCaptureSearch, dispatchSetActivated, dispatchSetPressed, dispatchSetSelected, dispatchStartTemporaryDetach, dispatchSystemUiVisibilityChanged, dispatchThawSelfOnly, dispatchTouchEvent, dispatchTrackballEvent, dispatchUnhandledMove, dispatchVisibilityChanged, dispatchWindowFocusChanged, dispatchWindowInsetsAnimationEnd, dispatchWindowInsetsAnimationPrepare, dispatchWindowInsetsAnimationProgress, dispatchWindowInsetsAnimationStart, dispatchWindowSystemUiVisiblityChanged, dispatchWindowVisibilityChanged, drawableStateChanged, drawChild, endViewTransition, findFocus, findOnBackInvokedDispatcherForChild, findViewsWithText, focusableViewAvailable, focusSearch, gatherTransparentRegion, getChildAt, getChildCount, getChildDrawingOrder, getChildDrawingOrder, getChildMeasureSpec, getChildStaticTransformation, getChildVisibleRect, getClipChildren, getClipToPadding, getDescendantFocusability, getFocusedChild, getLayoutAnimation, getLayoutAnimationListener, getLayoutMode, getLayoutTransition, getNestedScrollAxes, getOverlay, getPersistentDrawingCache, getTouchscreenBlocksFocus, hasFocus, hasTransientState, indexOfChild, invalidateChild, invalidateChildInParent, isAlwaysDrawnWithCacheEnabled, isAnimationCacheEnabled, isChildrenDrawingOrderEnabled, isChildrenDrawnWithCacheEnabled, isLayoutSuppressed, isMotionEventSplittingEnabled, isTransitionGroup, jumpDrawablesToCurrentState, layout, measureChild, measureChildren, measureChildWithMargins, notifySubtreeAccessibilityStateChanged, offsetDescendantRectToMyCoords, offsetRectIntoDescendantCoords, onAttachedToWindow, onCreateDrawableState, onDescendantInvalidated, onDetachedFromWindow, onInterceptHoverEvent, onInterceptTouchEvent, onNestedFling, onNestedPreFling, onNestedPrePerformAccessibilityAction, onNestedPreScroll, onNestedScroll, onNestedScrollAccepted, onRequestFocusInDescendants, onRequestSendAccessibilityEvent, onResolvePointerIcon, onStartNestedScroll, onStopNestedScroll, onViewAdded, onViewRemoved, recomputeViewAttributes, removeAllViews, removeAllViewsInLayout, removeDetachedView, removeView, removeViewAt, removeViewInLayout, removeViews, removeViewsInLayout, requestChildFocus, requestChildRectangleOnScreen, requestDisallowInterceptTouchEvent, requestFocus, requestSendAccessibilityEvent, requestTransparentRegion, restoreDefaultFocus, scheduleLayoutAnimation, setAddStatesFromChildren, setAlwaysDrawnWithCacheEnabled, setAnimationCacheEnabled, setChildrenDrawingCacheEnabled, setChildrenDrawingOrderEnabled, setChildrenDrawnWithCacheEnabled, setClipChildren, setClipToPadding, setDescendantFocusability, setLayoutAnimation, setLayoutAnimationListener, setLayoutMode, setLayoutTransition, setMotionEventSplittingEnabled, setOnHierarchyChangeListener, setPersistentDrawingCache, setStaticTransformationsEnabled, setTouchscreenBlocksFocus, setTransitionGroup, setWindowInsetsAnimationCallback, showContextMenuForChild, showContextMenuForChild, startActionModeForChild, startActionModeForChild, startLayoutAnimation, startViewTransition, suppressLayout, updateViewLayout`

### Methods inherited from class android.view.View

  `addFocusables, addOnAttachStateChangeListener, addOnLayoutChangeListener, addOnUnhandledKeyEventListener, animate, announceForAccessibility, autofill, autofill, awakenScrollBars, awakenScrollBars, awakenScrollBars, bringToFront, buildDrawingCache, buildDrawingCache, buildLayer, callOnClick, cancelDragAndDrop, cancelLongPress, cancelPendingInputEvents, canResolveLayoutDirection, canResolveTextAlignment, canResolveTextDirection, canScrollHorizontally, canScrollVertically, checkInputConnectionProxy, clearAnimation, clearPendingCredentialRequest, clearViewTranslationCallback, combineMeasuredStates, computeHorizontalScrollExtent, computeHorizontalScrollOffset, computeHorizontalScrollRange, computeScroll, computeSystemWindowInsets, computeVerticalScrollExtent, computeVerticalScrollOffset, computeVerticalScrollRange, createAccessibilityNodeInfo, createContextMenu, destroyDrawingCache, dispatchGenericMotionEvent, dispatchNestedFling, dispatchNestedPreFling, dispatchNestedPrePerformAccessibilityAction, dispatchNestedPreScroll, dispatchNestedScroll, dispatchPopulateAccessibilityEvent, draw, drawableHotspotChanged, findOnBackInvokedDispatcher, findViewById, findViewWithTag, fitSystemWindows, focusSearch, forceHasOverlappingRendering, forceLayout, generateDisplayHash, generateViewId, getAccessibilityDelegate, getAccessibilityLiveRegion, getAccessibilityNodeProvider, getAccessibilityPaneTitle, getAccessibilityTraversalAfter, getAccessibilityTraversalBefore, getAllowedHandwritingDelegatePackageName, getAllowedHandwritingDelegatorPackageName, getAlpha, getAnimation, getAnimationMatrix, getApplicationWindowToken, getAttributeResolutionStack, getAttributeSourceResourceMap, getAutofillHints, getAutofillId, getAutofillType, getAutofillValue, getBackground, getBackgroundTintBlendMode, getBackgroundTintList, getBackgroundTintMode, getBaseline, getBottom, getBottomFadingEdgeStrength, getBottomPaddingOffset, getCameraDistance, getClipBounds, getClipBounds, getClipToOutline, getContentCaptureSession, getContentDescription, getContentSensitivity, getContext, getContextMenuInfo, getDefaultFocusHighlightEnabled, getDefaultSize, getDisplay, getDrawableState, getDrawingCache, getDrawingCache, getDrawingCacheBackgroundColor, getDrawingCacheQuality, getDrawingRect, getDrawingTime, getElevation, getExplicitStyle, getFilterTouchesWhenObscured, getFitsSystemWindows, getFocusable, getFocusables, getFocusedRect, getForeground, getForegroundGravity, getForegroundTintBlendMode, getForegroundTintList, getForegroundTintMode, getFrameContentVelocity, getGlobalVisibleRect, getGlobalVisibleRect, getHandler, getHandwritingBoundsOffsetBottom, getHandwritingBoundsOffsetLeft, getHandwritingBoundsOffsetRight, getHandwritingBoundsOffsetTop, getHandwritingDelegateFlags, getHandwritingDelegatorCallback, getHasOverlappingRendering, getHeight, getHitRect, getHorizontalFadingEdgeLength, getHorizontalScrollbarHeight, getHorizontalScrollbarThumbDrawable, getHorizontalScrollbarTrackDrawable, getId, getImportantForAccessibility, getImportantForAutofill, getImportantForContentCapture, getKeepScreenOn, getKeyDispatcherState, getLabelFor, getLayerType, getLayoutDirection, getLayoutParams, getLeft, getLeftFadingEdgeStrength, getLeftPaddingOffset, getLocalVisibleRect, getLocationInSurface, getLocationInWindow, getLocationOnScreen, getMatrix, getMeasuredHeight, getMeasuredHeightAndState, getMeasuredState, getMeasuredWidth, getMeasuredWidthAndState, getMinimumHeight, getMinimumWidth, getNextClusterForwardId, getNextFocusDownId, getNextFocusForwardId, getNextFocusLeftId, getNextFocusRightId, getNextFocusUpId, getOnFocusChangeListener, getOutlineAmbientShadowColor, getOutlineProvider, getOutlineSpotShadowColor, getOverScrollMode, getPaddingBottom, getPaddingEnd, getPaddingLeft, getPaddingRight, getPaddingStart, getPaddingTop, getParent, getParentForAccessibility, getPendingCredentialCallback, getPendingCredentialRequest, getPivotX, getPivotY, getPointerIcon, getPreferKeepClearRects, getReceiveContentMimeTypes, getRequestedFrameRate, getResources, getRevealOnFocusHint, getRight, getRightFadingEdgeStrength, getRightPaddingOffset, getRootSurfaceControl, getRootView, getRootWindowInsets, getRotation, getRotationX, getRotationY, getScaleX, getScaleY, getScrollBarDefaultDelayBeforeFade, getScrollBarFadeDuration, getScrollBarSize, getScrollBarStyle, getScrollCaptureHint, getScrollIndicators, getScrollX, getScrollY, getSolidColor, getSourceLayoutResId, getStateDescription, getStateListAnimator, getSuggestedMinimumHeight, getSuggestedMinimumWidth, getSystemGestureExclusionRects, getSystemUiVisibility, getTag, getTag, getTextAlignment, getTextDirection, getTooltipText, getTop, getTopFadingEdgeStrength, getTopPaddingOffset, getTouchables, getTouchDelegate, getTransitionAlpha, getTransitionName, getTranslationX, getTranslationY, getTranslationZ, getUniqueDrawingId, getVerticalFadingEdgeLength, getVerticalScrollbarPosition, getVerticalScrollbarThumbDrawable, getVerticalScrollbarTrackDrawable, getVerticalScrollbarWidth, getViewTranslationResponse, getViewTreeObserver, getVisibility, getWidth, getWindowAttachCount, getWindowId, getWindowInsetsController, getWindowSystemUiVisibility, getWindowToken, getWindowVisibility, getWindowVisibleDisplayFrame, getX, getY, getZ, hasExplicitFocusable, hasFocusable, hasNestedScrollingParent, hasOnClickListeners, hasOnLongClickListeners, hasOverlappingRendering, hasPointerCapture, hasWindowFocus, inflate, invalidate, invalidate, invalidate, invalidateDrawable, invalidateOutline, isAccessibilityDataSensitive, isAccessibilityFocused, isAccessibilityHeading, isActivated, isAttachedToWindow, isAutoHandwritingEnabled, isClickable, isContentSensitive, isContextClickable, isCredential, isDirty, isDrawingCacheEnabled, isDuplicateParentStateEnabled, isEnabled, isFocusable, isFocusableInTouchMode, isFocused, isFocusedByDefault, isForceDarkAllowed, isHandwritingDelegate, isHapticFeedbackEnabled, isHardwareAccelerated, isHorizontalFadingEdgeEnabled, isHorizontalScrollBarEnabled, isHovered, isImportantForAccessibility, isImportantForAutofill, isImportantForContentCapture, isInEditMode, isInLayout, isInTouchMode, isKeyboardNavigationCluster, isLaidOut, isLayoutDirectionResolved, isLayoutRequested, isLongClickable, isNestedScrollingEnabled, isOpaque, isPaddingOffsetRequired, isPaddingRelative, isPivotSet, isPreferKeepClear, isPressed, isSaveEnabled, isSaveFromParentEnabled, isScreenReaderFocusable, isScrollbarFadingEnabled, isScrollContainer, isSelected, isShowingLayoutBounds, isShown, isSoundEffectsEnabled, isTemporarilyDetached, isTextAlignmentResolved, isTextDirectionResolved, isVerticalFadingEdgeEnabled, isVerticalScrollBarEnabled, isVisibleToUserForAutofill, keyboardNavigationClusterSearch, measure, mergeDrawableStates, offsetLeftAndRight, offsetTopAndBottom, onAnimationEnd, onAnimationStart, onApplyWindowInsets, onCancelPendingInputEvents, onCapturedPointerEvent, onCheckIsTextEditor, onConfigurationChanged, onCreateContextMenu, onCreateInputConnection, onCreateViewTranslationRequest, onCreateVirtualViewTranslationRequests, onDisplayHint, onDragEvent, onDraw, onDrawForeground, onDrawScrollBars, onFilterTouchEventForSecurity, onFinishInflate, onFinishTemporaryDetach, onFocusChanged, onGenericMotionEvent, onHoverChanged, onHoverEvent, onInitializeAccessibilityEvent, onInitializeAccessibilityNodeInfo, onKeyDown, onKeyLongPress, onKeyMultiple, onKeyPreIme, onKeyShortcut, onKeyUp, onOverScrolled, onPointerCaptureChange, onPopulateAccessibilityEvent, onProvideAutofillStructure, onProvideAutofillVirtualStructure, onProvideContentCaptureStructure, onProvideStructure, onProvideVirtualStructure, onReceiveContent, onRestoreInstanceState, onRtlPropertiesChanged, onSaveInstanceState, onScreenStateChanged, onScrollCaptureSearch, onScrollChanged, onSetAlpha, onSizeChanged, onStartTemporaryDetach, onTrackballEvent, onViewTranslationResponse, onVirtualViewTranslationResponses, onVisibilityAggregated, onVisibilityChanged, onWindowFocusChanged, onWindowSystemUiVisibilityChanged, onWindowVisibilityChanged, overScrollBy, performAccessibilityAction, performClick, performContextClick, performContextClick, performHapticFeedback, performHapticFeedback, performLongClick, performLongClick, performReceiveContent, playSoundEffect, post, postDelayed, postInvalidate, postInvalidate, postInvalidateDelayed, postInvalidateDelayed, postInvalidateOnAnimation, postInvalidateOnAnimation, postOnAnimation, postOnAnimationDelayed, refreshDrawableState, releasePointerCapture, removeCallbacks, removeOnAttachStateChangeListener, removeOnLayoutChangeListener, removeOnUnhandledKeyEventListener, requestApplyInsets, requestFitSystemWindows, requestFocus, requestFocus, requestFocusFromTouch, requestLayout, requestPointerCapture, requestRectangleOnScreen, requestRectangleOnScreen, requestUnbufferedDispatch, requestUnbufferedDispatch, requireViewById, resetPivot, resolveSize, resolveSizeAndState, restoreHierarchyState, saveAttributeDataForStyleable, saveHierarchyState, scheduleDrawable, scrollBy, scrollTo, sendAccessibilityEvent, sendAccessibilityEventUnchecked, setAccessibilityDataSensitive, setAccessibilityDelegate, setAccessibilityHeading, setAccessibilityLiveRegion, setAccessibilityPaneTitle, setAccessibilityTraversalAfter, setAccessibilityTraversalBefore, setActivated, setAllowClickWhenDisabled, setAllowedHandwritingDelegatePackage, setAllowedHandwritingDelegatorPackage, setAlpha, setAnimation, setAnimationMatrix, setAutofillHints, setAutofillId, setAutoHandwritingEnabled, setBackground, setBackgroundColor, setBackgroundDrawable, setBackgroundResource, setBackgroundTintBlendMode, setBackgroundTintList, setBackgroundTintMode, setBottom, setCameraDistance, setClickable, setClipBounds, setClipToOutline, setContentCaptureSession, setContentDescription, setContentSensitivity, setContextClickable, setDefaultFocusHighlightEnabled, setDrawingCacheBackgroundColor, setDrawingCacheEnabled, setDrawingCacheQuality, setDuplicateParentStateEnabled, setElevation, setEnabled, setFadingEdgeLength, setFilterTouchesWhenObscured, setFitsSystemWindows, setFocusable, setFocusable, setFocusableInTouchMode, setFocusedByDefault, setForceDarkAllowed, setForeground, setForegroundTintBlendMode, setForegroundTintList, setForegroundTintMode, setFrameContentVelocity, setHandwritingBoundsOffsets, setHandwritingDelegateFlags, setHandwritingDelegatorCallback, setHapticFeedbackEnabled, setHasTransientState, setHorizontalFadingEdgeEnabled, setHorizontalScrollBarEnabled, setHorizontalScrollbarThumbDrawable, setHorizontalScrollbarTrackDrawable, setHovered, setId, setImportantForAccessibility, setImportantForAutofill, setImportantForContentCapture, setIsCredential, setIsHandwritingDelegate, setKeepScreenOn, setKeyboardNavigationCluster, setLabelFor, setLayerPaint, setLayerType, setLayoutDirection, setLayoutParams, setLeft, setLeftTopRightBottom, setLongClickable, setMeasuredDimension, setMinimumHeight, setMinimumWidth, setNestedScrollingEnabled, setNextClusterForwardId, setNextFocusDownId, setNextFocusForwardId, setNextFocusLeftId, setNextFocusRightId, setNextFocusUpId, setOnApplyWindowInsetsListener, setOnCapturedPointerListener, setOnClickListener, setOnContextClickListener, setOnCreateContextMenuListener, setOnDragListener, setOnFocusChangeListener, setOnGenericMotionListener, setOnHoverListener, setOnKeyListener, setOnLongClickListener, setOnReceiveContentListener, setOnScrollChangeListener, setOnSystemUiVisibilityChangeListener, setOnTouchListener, setOutlineAmbientShadowColor, setOutlineProvider, setOutlineSpotShadowColor, setOverScrollMode, setPadding, setPaddingRelative, setPendingCredentialRequest, setPivotX, setPivotY, setPointerIcon, setPreferKeepClear, setPreferKeepClearRects, setPressed, setRenderEffect, setRequestedFrameRate, setRevealOnFocusHint, setRight, setRotation, setRotationX, setRotationY, setSaveEnabled, setSaveFromParentEnabled, setScaleX, setScaleY, setScreenReaderFocusable, setScrollBarDefaultDelayBeforeFade, setScrollBarFadeDuration, setScrollbarFadingEnabled, setScrollBarSize, setScrollBarStyle, setScrollCaptureCallback, setScrollCaptureHint, setScrollContainer, setScrollIndicators, setScrollIndicators, setScrollX, setScrollY, setSelected, setSoundEffectsEnabled, setStateDescription, setStateListAnimator, setSystemGestureExclusionRects, setSystemUiVisibility, setTag, setTag, setTextAlignment, setTextDirection, setTooltipText, setTop, setTouchDelegate, setTransitionAlpha, setTransitionName, setTransitionVisibility, setTranslationX, setTranslationY, setTranslationZ, setVerticalFadingEdgeEnabled, setVerticalScrollBarEnabled, setVerticalScrollbarPosition, setVerticalScrollbarThumbDrawable, setVerticalScrollbarTrackDrawable, setViewTranslationCallback, setWillNotCacheDrawing, setWillNotDraw, setX, setY, setZ, showContextMenu, showContextMenu, startActionMode, startActionMode, startAnimation, startDrag, startDragAndDrop, startNestedScroll, stopNestedScroll, toString, transformMatrixToGlobal, transformMatrixToLocal, unscheduleDrawable, unscheduleDrawable, updateDragShadow, verifyDrawable, willNotCacheDrawing, willNotDraw`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

### Methods inherited from interface android.view.ViewParent

  `canResolveLayoutDirection, canResolveTextAlignment, canResolveTextDirection, createContextMenu, getLayoutDirection, getParent, getParentForAccessibility, getTextAlignment, getTextDirection, isLayoutDirectionResolved, isLayoutRequested, isTextAlignmentResolved, isTextDirectionResolved, keyboardNavigationClusterSearch, requestFitSystemWindows, requestLayout`

## Constructor Details

  - (android.content.Context,com.here.sdk.mapview.MapViewOptions)" class="section detail">

### MapView

public MapView(android.content.Context context, [MapViewOptions](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview") options)

    Simple constructor to use when creating a map view from code.
Parameters:
    `context` - The Context the view is running in, through which it can access the current theme, resources, etc.

    `options` - Customization of view for example its map projection.
- (android.content.Context)" class="section detail">

### MapView

public MapView(android.content.Context context)

    Simple constructor to use when creating a map view from code.
Parameters:
    `context` - The Context the view is running in, through which it can access the current theme, resources, etc.
- (android.content.Context,android.util.AttributeSet)" class="section detail">

### MapView

public MapView(android.content.Context context, android.util.AttributeSet attrs)

    Creates a new instance.
Parameters:
    `context` - The Context the view is running in, through which it can access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag in an XML document.
- (android.content.Context,android.util.AttributeSet,int)" class="section detail">

### MapView

public MapView(android.content.Context context, android.util.AttributeSet attrs, int defStyleAttr)

    Creates a new instance.
Parameters:
    `context` - The Context the view is running in, through which it can access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag in an XML document.

    `defStyleAttr` - An attribute in the current theme that contains a reference to a style resource that supplies defaults values for the StyledAttributes. Can be 0 to not look for defaults.
- (com.here.sdk.core.engine.SDKNativeEngine,android.content.Context,android.util.AttributeSet,int)" class="section detail">

### MapView

public MapView([SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") engine, android.content.Context context, android.util.AttributeSet attrs, int defStyleAttr)

    Creates a new instance.
Parameters:
    `engine` - The SDKNativeEngine instance.

    `context` - The Context the view is running in, through which it can access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag in an XML document..

    `defStyleAttr` - An attribute in the current theme that contains a reference to a style resource that supplies defaults values for the StyledAttributes. Can be 0 to not look for defaults.
- (com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapview.MapViewOptions,android.content.Context,android.util.AttributeSet,int)" class="section detail">

### MapView

public MapView([SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") engine, [MapViewOptions](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview") options, android.content.Context context, android.util.AttributeSet attrs, int defStyleAttr)

    Creates a new instance.
Parameters:
    `engine` - The SDKNativeEngine instance.

    `options` - Customization of view for example its map projection.

    `context` - The Context the view is running in, through which it can access the current theme, resources, etc.

    `attrs` - A collection of attributes, as found associated with a tag in an XML document.

    `defStyleAttr` - An attribute in the current theme that contains a reference to a style resource that supplies defaults values for the StyledAttributes. Can be 0 to not look for defaults.

## Method Details

### setVisibility

public void setVisibility(int visibility)

    Sets the visibility of MapView. Visibilities of views pinned to MapView (see [`pinView(View, GeoCoordinates)`](#pinView(android.view.View,com.here.sdk.core.GeoCoordinates))) will not be affected by this method.
Overrides:
    `setVisibility` in class `android.view.View`

    Parameters:
    `visibility` - Desired visibility as one of `View.INVISIBLE`, `View.VISIBLE` or `View.GONE`.

### setPrimaryLanguage

public static void setPrimaryLanguage(@Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode)

    Set desired primary map display language for all instances of MapView. Applying a language change causes map to be redrawn.
    If `null` is passed or the specified language is not supported, local language of the region will be used, which is the default behaviour.
Parameters:
    `languageCode` - The code of the desired language, or `null` for default language.

### setSecondaryLanguage

public static void setSecondaryLanguage(@Nullable [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") languageCode)

    Set desired secondary map display language for all instances of MapView. Applying a language change causes map to be redrawn.
    If the specified language is not supported, local language of the region will be used. If null, no secondary map language will be used which is the default behaviour. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Parameters:
    `languageCode` - The code of the desired language, or @null to unset.

### getPrimaryLanguage

@Nullable public static [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") getPrimaryLanguage()

    Gets code of currently set primary map display language.
Returns:
    The code of currently set language or @null language.

### getSecondaryLanguage

@Nullable public static [LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core") getSecondaryLanguage()

    Gets code of currently set secondary map display language. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Returns:
    The code of currently set language or @null language.

### setShadowQuality

public static void setShadowQuality([ShadowQuality](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview") shadowQuality)

    Set desired shadow quality for all instances of MapView/MapSurface. The quality controls the size of the shadow maps and the cascade count. The default shadow quality is `ShadowQuality.MEDIUM`. MapViews can request to render shadows by feature. Enabling shadows has a performance impact and should be considered only for devices with sufficient performance. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Parameters:
    `shadowQuality` - The shadow quality.

### getShadowQuality

public static [ShadowQuality](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview") getShadowQuality()

    Gets the currently set shadow quality. The default shadow quality is `ShadowQuality.MEDIUM`. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Returns:
    The currently set shadow quality.

### onCreate

public void onCreate(android.os.Bundle bundle)

    Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods.
    Note: `SDKNativeEngine` must be already initialized before calling this method.
Parameters:
    `bundle` - The bundle which was passed to onCreate() method of the view owner

### onCreate

public void onCreate(android.os.Bundle bundle, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) identifier)

    Call this method in the onCreate() method of the lifecycle owner before calling any other MapView methods if there are multiple MapViews instances to (re)create.
    Note: `SDKNativeEngine` must be already initialized before calling this method.
Parameters:
    `bundle` - The bundle which was passed to onCreate() method of the view owner

    `identifier` - in case of multiple MapView instances use the same String which is passed to onSaveInstanceState() to identify each MapView.

### setOnReadyListener

public void setOnReadyListener([MapView.OnReadyListener](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview") readyListener)

    Sets the OnReadyListener, which will be notified once MapView initialization has been finished. It is highly recommended to put code that accesses map view related functionality inside [`MapView.OnReadyListener.onMapViewReady()`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener#onMapViewReady()) instead of directly in `Activity`'s `onResume()`.
Parameters:
    `readyListener` - The listener to be registered, or `null` to unregister any previously register listener.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### onResume

public void onResume()

    Call this method in the onResume() method of the lifecycle owner.

### onPause

public void onPause()

    Call this method in the onPause() method of the lifecycle owner.

### isValid

public boolean isValid()

    Returns whether this `MapView` is valid. An invalid `MapView` is non-functional. A `MapView` is considered valid only after [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) or [`onCreate(Bundle, String)`](#onCreate(android.os.Bundle,java.lang.String)) and before [`onDestroy()`](#onDestroy()) is called. `MapView` is also invalidated when the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") it is using is destroyed.
Specified by:
    [`isValid`](sdk-for-android-explore-api-reference-latestmapviewbase#isValid()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    `true` if this `MapView` is valid, `false` otherwise.

### onDestroy

public void onDestroy()

    Call this method in the onDestroy() method of the lifecycle owner

### onSaveInstanceState

public void onSaveInstanceState(android.os.Bundle bundle)

    Call this method in the onSaveInstance() method of the lifecycle owner.
Parameters:
    `bundle` - the bundle which was passed to lifecycle owner

### onSaveInstanceState

public void onSaveInstanceState(android.os.Bundle bundle, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) identifier)

    Call this method in the onSaveInstance() method of the lifecycle owner if multiple MapView instances are present. Each MapView instance should have its own identifier string which is passed to onSaveInstanceState() and onCreate() methods.
Parameters:
    `bundle` - The bundle which was passed to lifecycle owner.

    `identifier` - If multiple MapView instances are under the same lifecycle owner then provide a unique string to identify each MapView instance.

### pick

public void pick(@Nullable [MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview") filter, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewArea, @NonNull [MapViewBase.MapPickCallback](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview") callback)

    Returns all map content located inside the specified pick area. Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view's origin at (0, 0) which indicates the top-left corner of the map view.
Specified by:
    [`pick`](sdk-for-android-explore-api-reference-latestmapviewbase#pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `filter` -

    Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.

    `viewArea` -

    The rectangular pixel area of the view inside which map content will be picked. View area is relative to the map view's origin at (0, 0) at the top-left corner of the map view.

    `callback` -

    Callback to call with the result. This will be called on a main thread when pick operation completes.

### geoToViewCoordinates

@Nullable public [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") geoToViewCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoCoordinates)

    Converts geographical coordinates to view coordinates (in pixels).
    If specified, altitude of the input coordinates is interpreted as altitude above sea level. If not specified, the input coordinates are interpreted as being on ground elevation. The above distinction is only relevant when 3D terrain feature is enabled.

    The resulting view coordinates might be outside of current viewport, i.e. result might contain values less than zero or greater than view's dimensions.

    If the render surface is not attached, it will return `null`.
Specified by:
    [`geoToViewCoordinates`](sdk-for-android-explore-api-reference-latestmapviewbase#geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `geoCoordinates` -

    Geographical coordinates to convert.

    Returns:
    The view coordinates of the specified geographical point or `null` if there is no render surface attached.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

    See Also:
    - [`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")

### addLifecycleListener

public void addLifecycleListener(@NonNull [MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)

    Adds a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") to this map view. Adding the same object multiple times has no effect.
Specified by:
    [`addLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewbase#addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `lifecycleListener` - An object to be notified of lifecycle events.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### removeLifecycleListener

public void removeLifecycleListener(@NonNull [MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)

    Removes a [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview") from this map view. Trying to remove an object that was not added or was removed before has no effect.
Specified by:
    [`removeLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewbase#removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `lifecycleListener` - An object to stop being notified of lifecycle events.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### pinView

@Nullable public [MapView.ViewPin](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview") pinView(@NonNull android.view.View view, [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates)

    Pins a `View` to the `MapView` and returns a proxy object that can be used to control the pinning.
    Trying to pin a view that was already pinned or a view that has a parent has no effect and returns `null`.

    The altitude component of the coordinates, if set, is interpreted as above sea level. When not set, the coordinates are interpreted as at ground level.
Parameters:
    `view` - `View` to add.

    `coordinates` - `GeoCoordinates` to pin the view at.

    Returns:
    The handle to a pinned view, or `null` if the view could not be pinned to the map.

### unpinView

public void unpinView(@NonNull android.view.View view)

    Removes a [`MapView.ViewPin`](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview") from the `MapView` by specifying the corresponding view. Trying to unpin a view that was not pinned or was unpinned before has no effect.
Parameters:
    `view` - The view corresponding to the `ViewPin` to remove.

### getViewPins

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapView.ViewPin](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview")\> getViewPins()

    Returns a copy of the list of views currently pinned to the map view.
Returns:
    A copy of the list of view pins.

### viewToGeoCoordinates

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") viewToGeoCoordinates(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewCoordinates)

    Converts view coordinates to geographical coordinates.
    An optional altitude component of the resulting geographical coordinate is not set.

    If the view coordinates specify a point above a horizon, then the result is geographical coordinates of the point on a horizon below the specified view coordinates.

    The fog effect is ignored for the calculation, meaning that for the view point within the area covered by the fog, the result is geographical coordinates that would be displayed at the specified point if the fog effect was not applied.

    If the render surface is not attached, it will return `null`.
Specified by:
    [`viewToGeoCoordinates`](sdk-for-android-explore-api-reference-latestmapviewbase#viewToGeoCoordinates(com.here.sdk.core.Point2D)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `viewCoordinates` -

    Point inside the view to convert.

    Returns:
    The geographical coordinates under specified view point or `null` if there is no render surface attached.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

    See Also:
    - [`MapView.OnReadyListener`](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")

### getGestures

@NonNull public [Gestures](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") getGestures()

    Returns the gestures control object
Specified by:
    [`getGestures`](sdk-for-android-explore-api-reference-latestmapviewbase#getGestures()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`Gestures`](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures") control object

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### getPixelScale

public double getPixelScale()

    Gets the pixel scale factor used by this MapView.
    It is is used to support screen resolution and size independence. This value is a derivative of the device's screen pixel density and is a direct analog of pixel density from DisplayMetrics. It can be used to translate between physical pixels and density independent pixels according to formula:

    dp = px / pixel_scale
Specified by:
    [`getPixelScale`](sdk-for-android-explore-api-reference-latestmapviewbase#getPixelScale()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    current pixel scale factor, or 0.0 if MapView is not initialized

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### getViewportSize

public [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") getViewportSize()

    Gets the size of this map view in physical pixels.
    If internally the map view's render surface is not attached yet (see: [`MapViewLifecycleListener`](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")), or after the map view has been destroyed then a `Size2D` with zero width and height is returned.
Specified by:
    [`getViewportSize`](sdk-for-android-explore-api-reference-latestmapviewbase#getViewportSize()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    The viewport size in physical pixels, or Size2D(0.0,0.0) if MapView is not initialized

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### getFrameRate

public int getFrameRate()

    Gets maximum render frame rate in frames per second. The default value is 60 frames per second.
Specified by:
    [`getFrameRate`](sdk-for-android-explore-api-reference-latestmapviewbase#getFrameRate()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    Actual maximal render frame rate

### setFrameRate

public void setFrameRate(int value)

    Sets maximum render frame rate in frames per second.
Specified by:
    [`setFrameRate`](sdk-for-android-explore-api-reference-latestmapviewbase#setFrameRate(int)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `value` - Maximum render frame rate in frames per second. Setting to 0 disables automatic rendering for this view. Setting negative values has no effect.

### takeScreenshot

public void takeScreenshot([MapView.TakeScreenshotCallback](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback "interface in com.here.sdk.mapview") callback)

    Asynchronously retrieves a screenshot of current map view. Note that this may not work when the map view is currently not visible, for example, when an application is running in background and onPause() was called.
Parameters:
    `callback` - Completion handler called when the screenshot is completed

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### setWatermarkLocation

public void setWatermarkLocation(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") offset)

    Sets the position of the HERE logo watermark within the map view. By default, the watermark is aligned to the bottom-right corner of the view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2). It is recommended to change the default position only if necessary to avoid overlapping UI elements. The watermark should always be fully visible within the view. The anchor point on the watermark is its center (width/2, height/2), around which it will be placed in the map view. For map views smaller than 250 dip in both width and height, the watermark will not be shown.
Specified by:
    [`setWatermarkLocation`](sdk-for-android-explore-api-reference-latestmapviewbase#setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Parameters:
    `anchor` -

    Anchor point in normalized view coordinates \[0, 1\]. Map view's origin at (0, 0) indicates a top-left corner of the map view. Out of boundary anchor point values will be clamped to the \[0, 1\] range.

    `offset` -

    A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that allows shifting the watermark from the anchor point position in one or the other direction. For the quadrant of values expressing visible part of the map view negative offset shifts the watermark to the direction of the origin, positive - away from it. For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to the bottom. If specified offset will result in watermark being completely or partially out-of-view the offset will be adjusted internally so that watermark is fully visible. Offset is not being scaled when the map view size changes.

### getWatermarkSize

@NonNull public [Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core") getWatermarkSize()

    Returns the watermark size in physical pixels.
Specified by:
    [`getWatermarkSize`](sdk-for-android-explore-api-reference-latestmapviewbase#getWatermarkSize()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    Provides the size of the watermark in physical pixels.

### getCamera

@NonNull public [MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview") getCamera()

    Gets the camera control object for the map.
Specified by:
    [`getCamera`](sdk-for-android-explore-api-reference-latestmapviewbase#getCamera()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview") object for the map.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### getMapScene

@NonNull public [MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") getMapScene()

    Gets the map scene associated with this map view.
    This can be used to request different map schemes to be displayed in the map view, and to add and remove map items from the map.
Specified by:
    [`getMapScene`](sdk-for-android-explore-api-reference-latestmapviewbase#getMapScene()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`MapScene`](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview") associated with this map view.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### getMapContext

@NonNull public [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") getMapContext()

    Gets the map context associated with this map view.
Specified by:
    [`getMapContext`](sdk-for-android-explore-api-reference-latestmapviewbase#getMapContext()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") associated with this map view.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### getHereMap

@NonNull public [HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") getHereMap()

    Gets the HereMap associated with this map view.
Specified by:
    [`getHereMap`](sdk-for-android-explore-api-reference-latestmapviewbase#getHereMap()) in interface [`MapViewBase`](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")

    Returns:
    the [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") associated with this map view.

    Throws:
    [IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html) - if [`onCreate(Bundle)`](#onCreate(android.os.Bundle)) method was not called beforehand.

### setFixedSize

public void setFixedSize(int width, int height, double factor)

    Requests a fixed size to be used for rendering this MapView. Use this feature to render [`MapView`](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview") to a smaller size and let the system upscale to actual on-screen size. The new fixed size is expected to have the same aspect ratio as the on-screen size and the factor provided to match the factor applied to the on-screen size that leads to the new fixed size: - width = on-screen width \* factor - height = on-screen height \* factor Note: This feature is in beta state and thus there can be bugs and unexpected behavior.
Parameters:
    `width` - Fixed width to be used, in pixels.

    `height` - Fixed height to be used, in pixels.

    `factor` - Factor in between (0.0, 1.0\] by which screen size differs from fixed size.

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if factor is not inside (0.0, 1.0\].

    [UnsupportedOperationException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/UnsupportedOperationException.html) - if [`MapView`](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview") render mode is not MapRenderMode.SURFACE.
