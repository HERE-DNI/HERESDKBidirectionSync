---
title: "MapSurface (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapsurface"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapSurface

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
[`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public class
</span><span class="element-name type-name-label">MapSurface</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a>
implements
[MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")</span>

</div>

<div class="block">

Provides the ability to render a map into a provided rendering surface.
This enables the possibility to render a map into external displays like
Android Auto. If you want to use the map for a regular use case please
use the MapView instead.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-nested-class-summary"
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
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsurface-renderlistener"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapSurface.RenderListener</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Listener of MapSurface render events.

  </div>

  </div>

  </div>

  <div class="inherited-list">

  [`MapViewBase.MapPickCallback`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase-mappickcallback "interface in com.here.sdk.mapview")

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
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

      MapSurface()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapSurface(android.content.Context context)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapSurface(android.content.Context context,
       MapViewOptions options)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapSurface(MapViewOptions options)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
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

      addLifecycleListener(MapViewLifecycleListener lifecycleListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a MapViewLifecycleListener to this map view.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      attachSurface(android.content.Context context,
       android.view.Surface surface,
       int width,
       int height)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the surface on which the map will be rendered.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      attachSurface(android.content.Context context,
       android.view.Surface surface,
       int width,
       int height,
       MapSurface.RenderListener renderListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the surface on which the map will be rendered.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      destroy()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Destroys the map renderer and render surface, making this MapSurface
  invalid.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      destroySurface()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Destroys the rendering surface.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Point2D`](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      geoToViewCoordinates(GeoCoordinates geoCoordinates)

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

      getCamera()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the camera control object for the map

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFrameRate()

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

      getGestures()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the gestures control object.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`HereMap`](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getHereMap()

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

      getMapContext()

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

      getMapScene()

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

      getPixelScale()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the pixel scale factor used by this MapView.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`ShadowQuality`](sdk-for-android-explore-com-here-sdk-mapview-shadowquality "enum class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getShadowQuality()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets the currently set shadow quality.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Size2D`](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getViewportSize()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the viewport size of this MapView in physical pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Size2D`](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getWatermarkSize()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the watermark size in physical pixels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isValid()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns whether this MapSurface is valid.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onPause()

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

      onResume()

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

      pick(MapScene.MapPickFilter filter,
       Rectangle2D viewArea,
       MapViewBase.MapPickCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns all map content located inside the specified pick area.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      redraw(Runnable redrawFinished)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Redraws the map and reports back on completion.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeLifecycleListener(MapViewLifecycleListener lifecycleListener)

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

      setFrameRate(int value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets maximum render frame rate in frames per second.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOnReadyListener(MapView.OnReadyListener readyListener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the OnReadyListener, which will be notified once MapView
  initialization has been finished.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setShadowQuality(ShadowQuality shadowQuality)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Set desired shadow quality for all instances of MapSurface/MapView.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setWatermarkLocation(Anchor2D anchor,
       Point2D offset)

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

      takeScreenshot(MapView.TakeScreenshotCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously retrieves screenshot of current map view

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      viewToGeoCoordinates(Point2D viewCoordinates)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Converts view coordinates to geographical coordinates.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>()" class="section detail">

    ### MapSurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapSurface</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapViewOptions)"
    class="section detail">

    ### MapSurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapSurface</span><span class="parameters">([MapViewOptions](sdk-for-android-explore-com-here-sdk-mapview-mapviewoptions "class in com.here.sdk.mapview") options)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `options` - The options

    </div>
<div id="sdk-for-android-explore-<init>(android.content.Context)"
    class="section detail">

    ### MapSurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapSurface</span><span class="parameters">(android.content.Context context)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `context` - The Application context

    </div>
<div id="sdk-for-android-explore-<init>(android.content.Context,com.here.sdk.mapview.MapViewOptions)"
    class="section detail">

    ### MapSurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapSurface</span><span class="parameters">(android.content.Context context,
    [MapViewOptions](sdk-for-android-explore-com-here-sdk-mapview-mapviewoptions "class in com.here.sdk.mapview") options)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `options` - The options

    `context` - The Application context

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-isValid()" class="section detail">

    ### isValid

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isValid</span>()

    </div>

    <div class="block">

    Returns whether this MapSurface is valid. An invalid MapSurface is
    non-functional. A MapSurface is considered valid only after
    attachSurface(Context, Surface, int, int) and before destroy() is
    called. MapSurface is also invalidated when the SDKNativeEngine it
    is using is destroyed.

    </div>

    Specified by:  
    [`isValid`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#isValid()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    `true` if this `MapSurface` is valid, `false` otherwise.

    </div>
<div id="sdk-for-android-explore-destroy()" class="section detail">

    ### destroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()

    </div>

    <div class="block">

    Destroys the map renderer and render surface, making this MapSurface
    invalid. Call this method only when the render surface will no
    longer be used. isValid() will return false after this is called. It
    can be made valid again by setting render surface using
    attachSurface(Context, Surface, int, int) .

    </div>

    </div>
<div id="sdk-for-android-explore-setOnReadyListener(com.here.sdk.mapview.MapView.OnReadyListener)"
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

    </div>
<div id="sdk-for-android-explore-attachSurface(android.content.Context,android.view.Surface,int,int)"
    class="section detail">

    ### attachSurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">attachSurface</span><span class="parameters">(android.content.Context context,
    android.view.Surface surface, int width, int height)</span>

    </div>

    <div class="block">

    Sets the surface on which the map will be rendered. Throws exception
    if the surface cannot be used by HERESDK.

    </div>

    Parameters:  
    `context` - The Application context

    `surface` - The surface to render to.

    `width` - The width of the render surface in pixels.

    `height` - The height of the render surface in pixels.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if surface is invalid and cannot be used.

    </div>
<div id="sdk-for-android-explore-attachSurface(android.content.Context,android.view.Surface,int,int,com.here.sdk.mapview.MapSurface.RenderListener)"
    class="section detail">

    ### attachSurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">attachSurface</span><span class="parameters">(android.content.Context context,
    android.view.Surface surface, int width, int height, @NonNull
    [MapSurface.RenderListener](sdk-for-android-explore-com-here-sdk-mapview-mapsurface-renderlistener "interface in com.here.sdk.mapview") renderListener)</span>

    </div>

    <div class="block">

    Sets the surface on which the map will be rendered. Throws exception
    if the surface cannot be used by HERESDK. Note: This feature is in
    BETA state and thus there can be bugs and unexpected behavior.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    Parameters:  
    `context` - The Application context

    `surface` - The surface to render to.

    `width` - The width of the render surface in pixels.

    `height` - The height of the render surface in pixels.

    `renderListener` - A listener for render events. The listener will
    be released once
    [](sdk-for-android-explore-com-here-sdk-mapview-mapsurface#destroySurface())

        destroySurface()

    gets called.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if surface is invalid and cannot be used.

    </div>
<div id="sdk-for-android-explore-destroySurface()"
    class="section detail">

    ### destroySurface

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroySurface</span>()

    </div>

    <div class="block">

    Destroys the rendering surface.

    </div>

    </div>
<div id="sdk-for-android-explore-redraw(java.lang.Runnable)"
    class="section detail">

    ### redraw

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">redraw</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html"
    class="external-link"
    title="class or interface in java.lang">Runnable</a> redrawFinished)</span>

    </div>

    <div class="block">

    Redraws the map and reports back on completion.

    </div>

    Parameters:  
    `redrawFinished` -

    The runnable to be executed after completion.

    </div>
<div id="sdk-for-android-explore-pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)"
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
<div id="sdk-for-android-explore-geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)"
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
    if MapSurface object is not valid.

    See Also:  
    - [`MapView.OnReadyListener`](sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener "interface in com.here.sdk.mapview")

    </div>
<div id="sdk-for-android-explore-addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)"
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
    `lifecycleListener` -

    An object to be notified of lifecycle events.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)"
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
    `lifecycleListener` -

    An object to stop being notified of lifecycle events.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-onResume()" class="section detail">

    ### onResume

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onResume</span>()

    </div>

    <div class="block">

    Call this method in the onResume() method of the lifecycle owner.

    </div>

    </div>
<div id="sdk-for-android-explore-onPause()" class="section detail">

    ### onPause

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onPause</span>()

    </div>

    <div class="block">

    Call this method in the onPause() method of the lifecycle owner.

    </div>

    </div>
<div id="sdk-for-android-explore-viewToGeoCoordinates(com.here.sdk.core.Point2D)"
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
    if MapSurface object is not valid.

    See Also:  
    - [`MapView.OnReadyListener`](sdk-for-android-explore-com-here-sdk-mapview-mapview-onreadylistener "interface in com.here.sdk.mapview")

    </div>
<div id="sdk-for-android-explore-getGestures()"
    class="section detail">

    ### getGestures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Gestures](sdk-for-android-explore-com-here-sdk-gestures-gestures "class in com.here.sdk.gestures")</span> <span class="element-name">getGestures</span>()

    </div>

    <div class="block">

    Returns the gestures control object. Please note that there is no
    gesture support for the MapSurface at this point.

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
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getPixelScale()"
    class="section detail">

    ### getPixelScale

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getPixelScale</span>()

    </div>

    <div class="block">

    Gets the pixel scale factor used by this MapView. It is used to
    support screen resolution and size independence. This value is a
    derivative of the device's screen pixel density and is a direct
    analog of pixel density from DisplayMetrics. It can be used to
    translate between physical pixels and density independent pixels
    according to formula: dp = px / pixel_scale.

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
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getViewportSize()"
    class="section detail">

    ### getViewportSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">[Size2D](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")</span> <span class="element-name">getViewportSize</span>()

    </div>

    <div class="block">

    Returns the viewport size of this MapView in physical pixels.

    </div>

    Specified by:  
    [`getViewportSize`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getViewportSize()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    The viewport size in physical pixels

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getFrameRate()"
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

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-setFrameRate(int)"
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

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-takeScreenshot(com.here.sdk.mapview.MapView.TakeScreenshotCallback)"
    class="section detail">

    ### takeScreenshot

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">takeScreenshot</span><span class="parameters">([MapView.TakeScreenshotCallback](sdk-for-android-explore-com-here-sdk-mapview-mapview-takescreenshotcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Asynchronously retrieves screenshot of current map view

    </div>

    Parameters:  
    `callback` - Completion handler called when the screenshot is
    completed

    </div>
<div id="sdk-for-android-explore-setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)"
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

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getWatermarkSize()"
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

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-setShadowQuality(com.here.sdk.mapview.ShadowQuality)"
    class="section detail">

    ### setShadowQuality

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">setShadowQuality</span><span class="parameters">([ShadowQuality](sdk-for-android-explore-com-here-sdk-mapview-shadowquality "enum class in com.here.sdk.mapview") shadowQuality)</span>

    </div>

    <div class="block">

    Set desired shadow quality for all instances of MapSurface/MapView.
    The quality controls the size of the shadow maps and the cascade
    count. The default shadow quality is ShadowQuality.MEDIUM .
    MapSurfaces can request to render shadows by feature. Enabling
    shadows has a performance impact and should be considered only for
    devices with sufficient performance. Note: This feature is in beta
    state and thus there can be bugs and unexpected behavior.

    </div>

    Parameters:  
    `shadowQuality` - The shadow quality.

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getShadowQuality()"
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

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getCamera()"
    class="section detail">

    ### getCamera

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapCamera](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")</span> <span class="element-name">getCamera</span>()

    </div>

    <div class="block">

    Returns the camera control object for the map

    </div>

    Specified by:  
    [`getCamera`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase#getCamera()) in
    interface [`MapViewBase`](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

    Returns:  
    the
    [`MapCamera`](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")
    object for the map

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalStateException</code></a> -
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getMapScene()"
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
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getMapContext()"
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
    if MapSurface object is not valid.

    </div>
<div id="sdk-for-android-explore-getHereMap()"
    class="section detail">

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
    if MapSurface object is not valid.

    </div>

  </div>

</div>

