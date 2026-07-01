---
title: "MapViewBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapviewbase"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

All Known Implementing Classes:  
[`MapSurface`](sdk-for-android-explore-com-here-sdk-mapview-mapsurface "class in com.here.sdk.mapview"),
[`MapView`](sdk-for-android-explore-com-here-sdk-mapview-mapview "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">MapViewBase</span>

</div>

<div class="block">

Represents the available public API from MapView .

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Interface</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapviewbase-mappickcallback"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapViewBase.MapPickCallback</code></a></td>
  <td><div class="block">
  Callback for a pick request.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>addLifecycleListener(MapViewLifecycleListener lifecycleListener)</code></pre></td>
  <td><div class="block">
  Adds a MapViewLifecycleListener to this map view.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-point2d"
  title="class in com.here.sdk.core"><code>Point2D</code></a></td>
  <td><pre><code>geoToViewCoordinates(GeoCoordinates geoCoordinates)</code></pre></td>
  <td><div class="block">
  Converts geographical coordinates to view coordinates (in pixels).
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera"
  title="class in com.here.sdk.mapview"><code>MapCamera</code></a></td>
  <td><pre><code>getCamera()</code></pre></td>
  <td><div class="block">
  Gets the camera to control the view for the map.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>getFrameRate()</code></pre></td>
  <td><div class="block">
  Gets maximum render frame rate in frames per second.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-gestures-gestures"
  title="class in com.here.sdk.gestures"><code>Gestures</code></a></td>
  <td><pre><code>getGestures()</code></pre></td>
  <td><div class="block">
  Gets the gestures control object.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-heremap"
  title="class in com.here.sdk.mapview"><code>HereMap</code></a></td>
  <td><pre><code>getHereMap()</code></pre></td>
  <td><div class="block">
  Gets the HereMap associated with this map view.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext"
  title="class in com.here.sdk.mapview"><code>MapContext</code></a></td>
  <td><pre><code>getMapContext()</code></pre></td>
  <td><div class="block">
  Gets the map context associated with this map view.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-mapscene"
  title="class in com.here.sdk.mapview"><code>MapScene</code></a></td>
  <td><pre><code>getMapScene()</code></pre></td>
  <td><div class="block">
  Gets the map scene associated with this map view.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>getPixelScale()</code></pre></td>
  <td><div class="block">
  Gets the pixel scale factor used by this MapView .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-size2d"
  title="class in com.here.sdk.core"><code>Size2D</code></a></td>
  <td><pre><code>getViewportSize()</code></pre></td>
  <td><div class="block">
  Gets the size of this map view in physical pixels.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-size2d"
  title="class in com.here.sdk.core"><code>Size2D</code></a></td>
  <td><pre><code>getWatermarkSize()</code></pre></td>
  <td><div class="block">
  Returns the watermark size in physical pixels.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isValid()</code></pre></td>
  <td><div class="block">
  Returns true if this instance is valid, false otherwise.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>pick(MapScene.MapPickFilter filter,
   Rectangle2D viewArea,
   MapViewBase.MapPickCallback callback)</code></pre></td>
  <td><div class="block">
  Returns all map content located inside the specified pick area.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>removeLifecycleListener(MapViewLifecycleListener lifecycleListener)</code></pre></td>
  <td><div class="block">
  Removes a MapViewLifecycleListener from this map view.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setFrameRate(int value)</code></pre></td>
  <td><div class="block">
  Sets maximum render frame rate in frames per second.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setWatermarkLocation(Anchor2D anchor,
   Point2D offset)</code></pre></td>
  <td><div class="block">
  Sets the position of the HERE logo watermark within the map view.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>viewToGeoCoordinates(Point2D viewCoordinates)</code></pre></td>
  <td><div class="block">
  Converts view coordinates (in pixels) to geographical coordinates.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="viewToGeoCoordinates(com.here.sdk.core.Point2D)"
    class="section detail">

    ### viewToGeoCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">viewToGeoCoordinates</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") viewCoordinates)</span>

    </div>

    <div class="block">

    Converts view coordinates (in pixels) to geographical coordinates.
    An optional altitude component of the resulting geographical
    coordinate is not set. If the view coordinates specify a point above
    a horizon, then the result is geographical coordinates of the point
    on a horizon below the specified view coordinates. The fog effect is
    ignored for the calculation, meaning that for the view point within
    the area covered by the fog, the result is geographical coordinates
    that would be displayed at the specified point if the fog effect was
    not applied. If the render surface is not attached, it will return
    null .

    </div>

    Parameters:  
    `viewCoordinates` -

    Point inside the view to convert.

    Returns:  
    The geographical coordinates under specified view point or `null` if
    there is no render surface attached.

    </div>

  - <div id="geoToViewCoordinates(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### geoToViewCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type">[Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core")</span> <span class="element-name">geoToViewCoordinates</span><span class="parameters">(@NonNull
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

    Parameters:  
    `geoCoordinates` -

    Geographical coordinates to convert.

    Returns:  
    The view coordinates of the specified geographical point or `null`
    if there is no render surface attached.

    </div>

  - <div id="setWatermarkLocation(com.here.sdk.core.Anchor2D,com.here.sdk.core.Point2D)"
    class="section detail">

    ### setWatermarkLocation

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setWatermarkLocation</span><span class="parameters">(@NonNull
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

  - <div id="addLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)"
    class="section detail">

    ### addLifecycleListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">addLifecycleListener</span><span class="parameters">(@NonNull
    [MapViewLifecycleListener](sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)</span>

    </div>

    <div class="block">

    Adds a MapViewLifecycleListener to this map view. Adding the same
    object multiple times has no effect.

    </div>

    Parameters:  
    `lifecycleListener` -

    An object to be notified of lifecycle events.

    </div>

  - <div id="removeLifecycleListener(com.here.sdk.mapview.MapViewLifecycleListener)"
    class="section detail">

    ### removeLifecycleListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">removeLifecycleListener</span><span class="parameters">(@NonNull
    [MapViewLifecycleListener](sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener "interface in com.here.sdk.mapview") lifecycleListener)</span>

    </div>

    <div class="block">

    Removes a MapViewLifecycleListener from this map view. Trying to
    remove an object that was not added or was removed before has no
    effect.

    </div>

    Parameters:  
    `lifecycleListener` -

    An object to stop being notified of lifecycle events.

    </div>

  - <div id="pick(com.here.sdk.mapview.MapScene.MapPickFilter,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapViewBase.MapPickCallback)"
    class="section detail">

    ### pick

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">pick</span><span class="parameters">(@Nullable
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

  - <div id="isValid()" class="section detail">

    ### isValid

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isValid</span>()

    </div>

    <div class="block">

    Returns true if this instance is valid, false otherwise. It will be
    made It will be made invalid when the corresponding SDKNativeEngine
    is destroyed.

    </div>

    Returns:  
    Indicates whether this instance is valid.

    </div>

  - <div id="getCamera()" class="section detail">

    ### getCamera

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[MapCamera](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")</span> <span class="element-name">getCamera</span>()

    </div>

    <div class="block">

    Gets the camera to control the view for the map.

    </div>

    Returns:  
    The camera to control the view for the map.

    </div>

  - <div id="getGestures()" class="section detail">

    ### getGestures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[Gestures](sdk-for-android-explore-com-here-sdk-gestures-gestures "class in com.here.sdk.gestures")</span> <span class="element-name">getGestures</span>()

    </div>

    <div class="block">

    Gets the gestures control object.

    </div>

    Returns:  
    The gestures control object for setting up the capture of gestures.

    </div>

  - <div id="getMapScene()" class="section detail">

    ### getMapScene

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[MapScene](sdk-for-android-explore-com-here-sdk-mapview-mapscene "class in com.here.sdk.mapview")</span> <span class="element-name">getMapScene</span>()

    </div>

    <div class="block">

    Gets the map scene associated with this map view.

    </div>

    Returns:  
    Map scene associated with this map view.

    </div>

  - <div id="getMapContext()" class="section detail">

    ### getMapContext

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")</span> <span class="element-name">getMapContext</span>()

    </div>

    <div class="block">

    Gets the map context associated with this map view.

    </div>

    Returns:  
    Map context associated with this map view.

    </div>

  - <div id="getHereMap()" class="section detail">

    ### getHereMap

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[HereMap](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview")</span> <span class="element-name">getHereMap</span>()

    </div>

    <div class="block">

    Gets the HereMap associated with this map view.

    </div>

    Returns:  
    Here Map associated with this map view.

    </div>

  - <div id="getViewportSize()" class="section detail">

    ### getViewportSize

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[Size2D](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")</span> <span class="element-name">getViewportSize</span>()

    </div>

    <div class="block">

    Gets the size of this map view in physical pixels. If internally the
    map view's render surface is not attached yet (see:
    MapViewLifecycleListener ), or after the map view has been destroyed
    then a Size2D with zero width and height is returned.

    </div>

    Returns:  
    The size of this map view in physical pixels.

    </div>

  - <div id="getFrameRate()" class="section detail">

    ### getFrameRate

    <div class="member-signature">

    <span class="return-type">int</span> <span class="element-name">getFrameRate</span>()

    </div>

    <div class="block">

    Gets maximum render frame rate in frames per second.

    </div>

    Returns:  
    Maximum render frame rate in frames per second.

    </div>

  - <div id="setFrameRate(int)" class="section detail">

    ### setFrameRate

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setFrameRate</span><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets maximum render frame rate in frames per second. Setting to 0
    disables automatic rendering for this view. Setting negative values
    has no effect. The default value is 60 frames per second.

    </div>

    Parameters:  
    `value` -

    Maximum render frame rate in frames per second.

    </div>

  - <div id="getPixelScale()" class="section detail">

    ### getPixelScale

    <div class="member-signature">

    <span class="return-type">double</span> <span class="element-name">getPixelScale</span>()

    </div>

    <div class="block">

    Gets the pixel scale factor used by this MapView . It is used to
    support screen resolution and size independence. This value is a
    derivative of the device's screen pixel density and is a direct
    analog of pixel density from DisplayMetrics. It can be used to
    translate between physical pixels and density-independent pixels
    according to the formula: dp = px / pixelScale.

    </div>

    Returns:  
    The pixel scale factor used by this `MapView`. Pixel scale is 0.0 if
    the map view is not initialized.

    </div>

  - <div id="getWatermarkSize()" class="section detail">

    ### getWatermarkSize

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type">[Size2D](sdk-for-android-explore-com-here-sdk-core-size2d "class in com.here.sdk.core")</span> <span class="element-name">getWatermarkSize</span>()

    </div>

    <div class="block">

    Returns the watermark size in physical pixels.

    </div>

    Returns:  
    Provides the size of the watermark in physical pixels.

    </div>

  </div>

</div>

