---
title: "MapCameraUpdateFactory (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdatefactory"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapCameraUpdateFactory →
com.here.NativeBase → com.here.sdk.mapview.MapCameraUpdateFactory

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapCameraUpdateFactory</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Factory for creating MapCameraUpdate to change map's camera. For some
factory methods you can apply an additional padding in pixels by setting
a viewRectangle parameter based on the current size of the map view: int
leftPaddingInPixels = 5; int rightPaddingInPixels = 5; int
topPaddingInPixels = 5; int bottomPaddingInPixels = 5; int
horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
int verticalPaddingInPixels = topPaddingInPixels +
bottomPaddingInPixels; Point2D origin = new Point2D(leftPaddingInPixels,
topPaddingInPixels); Size2D sizeInPixels = new
Size2D(mapView.getWidth() - horizontalPaddingInPixels,
mapView.getHeight() - verticalPaddingInPixels); Rectangle2D
paddedViewRectangle = new Rectangle2D(origin, sizeInPixels); The origin
indicates the top-left corner of the rectangle. An origin of (0, 0)
indicates also the top-left corner of the map's viewport.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Concrete Methods

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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>compositeUpdate(List&lt;MapCameraUpdate&gt; mapCameraUpdates)</code></pre></td>
  <td><div class="block">
  Creates a composite camera update from a list of camera updates.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoBox target)</code></pre></td>
  <td><div class="block">
  Creates an update to look at the given geo-box, preserving current
  orientation and zooming at the center of viewport.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoBox target,
   GeoOrientationUpdate orientation,
   Rectangle2D viewRectangle)</code></pre></td>
  <td><div class="block">
  Create an update to look at the given geo-box and fit it inside the
  given rectangle.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoBox target,
   Rectangle2D viewRectangle)</code></pre></td>
  <td><div class="block">
  Creates an update to look at the given geo-box and fit it inside the
  given rectangle, preserving current orientation and zooming at the
  center of view rectangle.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoCoordinatesUpdate target)</code></pre></td>
  <td><div class="block">
  Creates an update to position the map camera to look at the given
  target, preserving the current orientation at look-at target and map
  measure.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoCoordinatesUpdate target,
   GeoOrientationUpdate orientation)</code></pre></td>
  <td><div class="block">
  Creates an update to position the map camera to look at the given target
  with the given orientation preserving the current map measure (zoom
  level/distance/scale) Any target or orientation sub-element value that
  is not finite will be excluded from the update.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoCoordinatesUpdate target,
   GeoOrientationUpdate orientation,
   MapMeasure measure)</code></pre></td>
  <td><div class="block">
  Creates an update to position the map camera to look at the given target
  with the given orientation and map measure.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoCoordinatesUpdate target,
   GeoOrientationUpdate orientation,
   List&lt;GeoCoordinates&gt; points,
   Rectangle2D viewRectangle,
   MapMeasure minMeasure,
   MapMeasure maxMeasure)</code></pre></td>
  <td><div class="block">
  Creates an update to position the camera to look at the given target
  with the given orientation and obeying map measure limits, so that the
  given geo locations are inside the given rectangle.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(GeoCoordinatesUpdate target,
   MapMeasure measure)</code></pre></td>
  <td><div class="block">
  Creates an update to position the map camera to look at the given target
  with the given map measure preserving the current orientation at look-at
  target.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookAt(List&lt;GeoCoordinates&gt; points,
   Rectangle2D viewRectangle,
   GeoOrientationUpdate orientation,
   MapMeasure measureLimit)</code></pre></td>
  <td><div class="block">
  Create an update to look at the given geo locations and fit them inside
  the given rectangle, in accordance with a map measure limit.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookToMatch(GeoCoordinates geoPoint,
   Point2D viewPoint)</code></pre></td>
  <td><div class="block">
  Creates an update to position the map camera to look at the map with the
  given geo point located at the given view point.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>lookToMatch(GeoCoordinates geoPoint,
   Point2D viewPoint,
   GeoOrientationUpdate orientation,
   MapMeasure measure)</code></pre></td>
  <td><div class="block">
  Creates an update to position the map camera to look at the map with the
  given orientation and map measure and with the given geo point located
  at the given view point.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>orbitBy(GeoOrientationUpdate delta,
   Point2D origin)</code></pre></td>
  <td><div class="block">
  Creates an update to orbit map camera around a pixel origin by specified
  geodetic orientation delta.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>panBy(double xOffset,
   double yOffset)</code></pre></td>
  <td><div class="block">
  Creates an update to pan map camera over the map by the specified number
  of pixels in the x and y direction starting from current principal point
  position.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>rotateBy(GeoOrientationUpdate delta)</code></pre></td>
  <td><div class="block">
  Creates an update to change map camera orientation by specified geodetic
  orientation delta.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>setNormalizedPrincipalPoint(Anchor2D principalPoint)</code></pre></td>
  <td><div class="block">
  Creates an update to change the map camera's principal point (where the
  view vector intersects the image plane - default is (0.5, 0.5)).
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>setPrincipalPoint(Point2D principalPoint)</code></pre></td>
  <td><div class="block">
  Creates an update to change the map camera's principal point (where the
  view vector intersects the image plane - default is the center of the
  view).
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>setVerticalFieldOfView(double verticalFieldOfView)</code></pre></td>
  <td><div class="block">
  Creates an update to change the vertical field of view of the map
  camera.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>zoomBy(double factor,
   Point2D origin)</code></pre></td>
  <td><div class="block">
  Creates an update to zoom map camera by a given factor preserving a
  given focus point.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate"
  title="class in com.here.sdk.mapview"><code>MapCameraUpdate</code></a></td>
  <td><pre><code>zoomTo(double zoomLevel)</code></pre></td>
  <td><div class="block">
  Creates an update to move map camera's viewpoint to a particular zoom
  level by adjusting its position.
  </div></td>
  </tr>
  </tbody>
  </table>

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

- <div id="method-detail" class="section method-details">

  - <div id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinatesUpdate](sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate "class in com.here.sdk.core") target)</span>

    </div>

    <div class="block">

    Creates an update to position the map camera to look at the given
    target, preserving the current orientation at look-at target and map
    measure. Any target sub-element value that is not finite will be
    excluded from the update. The altitude of the target point is
    ignored. Any subsequent camera updates and animations will consider
    the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    The look-at target position in geodetic coordinates, altitude is
    ignored, the target is considered to be located on the ground.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinatesUpdate](sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation)</span>

    </div>

    <div class="block">

    Creates an update to position the map camera to look at the given
    target with the given orientation preserving the current map measure
    (zoom level/distance/scale) Any target or orientation sub-element
    value that is not finite will be excluded from the update. The
    altitude of the target point is ignored. Any subsequent camera
    updates and animations will consider the target point as being
    located on the ground.

    </div>

    Parameters:  
    `target` -

    The look-at target position in geodetic coordinates.

    `orientation` -

    Geodetic orientation at look-at target.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinatesUpdate](sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate "class in com.here.sdk.core") target,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") measure)</span>

    </div>

    <div class="block">

    Creates an update to position the map camera to look at the given
    target with the given map measure preserving the current orientation
    at look-at target. Any target sub-element value that is not finite
    will be excluded from the update. If the map measure is not valid,
    the current map camera distance to the target point is preserved.
    The altitude of the target point is ignored. Any subsequent camera
    updates and animations will consider the target point as being
    located on the ground.

    </div>

    Parameters:  
    `target` -

    The look-at target position in geodetic coordinates.

    `measure` -

    The desired map measure.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinatesUpdate](sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") measure)</span>

    </div>

    <div class="block">

    Creates an update to position the map camera to look at the given
    target with the given orientation and map measure. Any target or
    orientation sub-element value that is not finite will be excluded
    from the update. If the map measure is not valid, the current map
    camera distance to the target point is preserved. The altitude of
    the target point is ignored. Any subsequent camera updates and
    animations will consider the target point as being located on the
    ground.

    </div>

    Parameters:  
    `target` -

    The look-at target position in geodetic coordinates.

    `orientation` -

    Geodetic orientation at look-at target.

    `measure` -

    The desired map measure.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)"
    class="section detail">

    ### lookToMatch

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookToMatch</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") geoPoint,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") viewPoint,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") measure)</span>

    </div>

    <div class="block">

    Creates an update to position the map camera to look at the map with
    the given orientation and map measure and with the given geo point
    located at the given view point. The altitude of the target point is
    ignored. Any subsequent camera updates and animations will consider
    the target point as being located on the ground. Note that this is a
    beta release of this feature, so there could be a few bugs and
    unexpected behaviors. Related APIs may change for new releases
    without a deprecation process.

    </div>

    Parameters:  
    `geoPoint` -

    The geo point that will be matched to the given view point. Note:
    the geo point will differ from the look at target of the camera.
    After this update the camera will still look at the principal point
    and therefore the look at target will be different from the geo
    point, since the geo point will correspond to the given view point
    and the look at target will correspond to the principal point. Look
    at target and the geo point will be identical only if the given view
    point is identical to the principal point.

    `viewPoint` -

    View point coordinates in pixels.

    `orientation` -

    Geodetic orientation at look-at target.

    `measure` -

    The desired map measure.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D)"
    class="section detail">

    ### lookToMatch

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookToMatch</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") geoPoint,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") viewPoint)</span>

    </div>

    <div class="block">

    Creates an update to position the map camera to look at the map with
    the given geo point located at the given view point. Note that this
    is a beta release of this feature, so there could be a few bugs and
    unexpected behaviors. Related APIs may change for new releases
    without a deprecation process. The altitude of the target point is
    ignored. Any subsequent camera updates and animations will consider
    the target point as being located on the ground.

    </div>

    Parameters:  
    `geoPoint` -

    The geo point that will be matched to the given view point. Note:
    the geo point will differ from the look at target of the camera.
    After this update the camera will still look at the principal point
    and therefore the look at target will be different from the geo
    point, since the geo point will correspond to the given view point
    and the look at target will correspond to the principal point. Look
    at target and the geo point will be identical only if the given view
    point is identical to the principal point.

    `viewPoint` -

    View point coordinates in pixels.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> points,
    @NonNull
    [Rectangle2D](sdk-for-android-explore-com-here-sdk-core-rectangle2d "class in com.here.sdk.core") viewRectangle,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") measureLimit)</span>

    </div>

    <div class="block">

    Create an update to look at the given geo locations and fit them
    inside the given rectangle, in accordance with a map measure limit.
    If the provided points list is empty, no update will be applied to
    the camera. If the viewRectangle parameter is invalid, fully or
    partially outside the map view, then the entire map viewport will be
    used as viewRectangle . Thus, no padding will be applied. A
    viewRectangle is considered invalid, when its width or height are
    negative or zero, its origin coordinates (x, y) are invalid, when
    they are negative. All viewRectangle values need to be finite to be
    considered as valid. If measure limit is not valid, no update will
    be applied to the map camera. The altitude of the target points is
    ignored. Any subsequent camera updates and animations will consider
    the target point as being located on the ground.

    </div>

    Parameters:  
    `points` -

    Array of points in geodetic space that should be visible inside the
    given view rectangle.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates inside which the
    geographical target area is displayed.

    `orientation` -

    Geodetic orientation at the new calculated target point.

    `measureLimit` -

    Map measure limit:

    - as distance: the minimum distance from map camera to earth surface
      at the center of the view rectangle in meters. The map camera
      should not be positioned closer to the center of view rectangle
      than this.
    - as zoom level: the maximum zoom level for the new map camera
      state. Internally converted to minimum distance from map camera to
      earth surface at the center of view rectangle in meters. This is
      not the zoom level for the calculated lookAt target point. Can be
      used to not zoom closer than a given level.
    - as scale: the minimum scale for the new map camera state.
      Internally converted to minimum distance from map camera to earth
      surface at the center of view rectangle in meters. This is not the
      scale for the calculated lookAt target point.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapMeasure,com.here.sdk.mapview.MapMeasure)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoCoordinatesUpdate](sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> points,
    @NonNull
    [Rectangle2D](sdk-for-android-explore-com-here-sdk-core-rectangle2d "class in com.here.sdk.core") viewRectangle,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") minMeasure,
    @NonNull
    [MapMeasure](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure "class in com.here.sdk.mapview") maxMeasure)</span>

    </div>

    <div class="block">

    Creates an update to position the camera to look at the given target
    with the given orientation and obeying map measure limits, so that
    the given geo locations are inside the given rectangle. Such
    position update can possibly not be found. Any target or orientation
    sub-element value that is not finite will be excluded from the
    update. If the provided points list is empty, no update will be
    applied to the map camera. If the viewRectangle parameter is
    invalid, fully or partially outside the map view, then the entire
    map viewport will be used as viewRectangle . Thus, no padding will
    be applied. A viewRectangle is considered invalid, when its width or
    height are negative or zero, its origin coordinates (x, y) are
    invalid, when they are negative. If map measures are not valid, no
    update will be applied to the map camera. The altitude of the target
    points is ignored. Any subsequent camera updates and animations will
    consider the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    The look-at target position in geodetic coordinates.

    `orientation` -

    Geodetic orientation at look-at target.

    `points` -

    Array of points in geodetic space that should be visible inside the
    given view rectangle.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates inside which the
    geographical points are displayed.

    `minMeasure` -

    Minimum map measure:

    - as distance: the minimum distance from map camera to earth surface
      at the look-at target in meters. The map camera should not be
      positioned closer to target than this.
    - as zoom level: the maximum zoom level for the new map camera
      state. Internally converted to minimum distance from map camera to
      earth surface at the look-at target in meters. Can be used to not
      zoom closer than a given level.
    - as scale: the minimum scale for the new map camera state.
      Internally converted to minimum distance from map camera to earth
      surface at the look-at target in meters.

    `maxMeasure` -

    Maximum map measure:

    - as distance: the maximum distance from map camera to earth surface
      at the look-at target in meters. The map camera should not be
      positioned further from target than this.
    - as zoom level: the minimum zoom level for the new map camera
      state. Internally converted to minimum distance from map camera to
      earth surface at the look-at target in meters. Can be used to not
      zoom further than a given level.
    - as scale: the maximum scale for the new map camera state.
      Internally converted to minimum distance from map camera to earth
      surface at the look-at target in meters.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") target,
    @NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") orientation,
    @NonNull
    [Rectangle2D](sdk-for-android-explore-com-here-sdk-core-rectangle2d "class in com.here.sdk.core") viewRectangle)</span>

    </div>

    <div class="block">

    Create an update to look at the given geo-box and fit it inside the
    given rectangle. If geoBox is not valid, no update will be applied
    to the map camera. If the viewRectangle parameter is invalid, fully
    or partially outside the map view, then the entire map viewport will
    be used as viewRectangle . Thus, no padding will be applied. A
    viewRectangle is considered invalid, when its width or height are
    negative or zero, its origin coordinates (x, y) are invalid, when
    they are negative. All viewRectangle values need to be finite to be
    considered as valid. In cases where it is not possible to find a
    solution for the given parameters, the resulting MapCameraUpdate
    will not change the map camera. The altitude of the target points is
    ignored. Any subsequent camera updates and animations will consider
    the target point as being located on the ground.

    </div>

    Parameters:  
    `target` -

    Geodetic box that should be visible inside the given view rectangle.

    `orientation` -

    Geodetic orientation at the target point.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates inside which the
    geographical target area is displayed.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.Rectangle2D)"
    class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") target,
    @NonNull
    [Rectangle2D](sdk-for-android-explore-com-here-sdk-core-rectangle2d "class in com.here.sdk.core") viewRectangle)</span>

    </div>

    <div class="block">

    Creates an update to look at the given geo-box and fit it inside the
    given rectangle, preserving current orientation and zooming at the
    center of view rectangle. If geoBox is not valid, no update will be
    applied to the map camera. If the viewRectangle parameter is
    invalid, fully or partially outside the map view, then the entire
    map viewport will be used as viewRectangle . Thus, no padding will
    be applied. A viewRectangle is considered invalid, when its width or
    height are negative or zero, its origin coordinates (x, y) are
    invalid, when they are negative. In cases where it is not possible
    to find a solution for the given parameters, the resulting
    MapCameraUpdate will not change the map camera. The altitude of the
    target points is ignored. Any subsequent camera updates and
    animations will consider the target point as being located on the
    ground.

    </div>

    Parameters:  
    `target` -

    Geodetic box that should be visible inside the given view rectangle.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="lookAt(com.here.sdk.core.GeoBox)" class="section detail">

    ### lookAt

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">lookAt</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") target)</span>

    </div>

    <div class="block">

    Creates an update to look at the given geo-box, preserving current
    orientation and zooming at the center of viewport. If geoBox is not
    valid, no update will be applied to the map camera. The altitude of
    the target points is ignored. Any subsequent camera updates and
    animations will consider the target point as being located on the
    ground.

    </div>

    Parameters:  
    `target` -

    Geodetic box that should be visible inside the viewport rectangle.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="panBy(double,double)" class="section detail">

    ### panBy

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">panBy</span><span class="parameters">(double xOffset,
    double yOffset)</span>

    </div>

    <div class="block">

    Creates an update to pan map camera over the map by the specified
    number of pixels in the x and y direction starting from current
    principal point position.

    </div>

    Parameters:  
    `xOffset` -

    X offset in pixels

    `yOffset` -

    Y offset in pixels

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D)"
    class="section detail">

    ### orbitBy

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">orbitBy</span><span class="parameters">(@NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") delta,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Creates an update to orbit map camera around a pixel origin by
    specified geodetic orientation delta. If the origin cannot be
    converted to geo coordinates, no update will be applied to the map
    camera. Orientation elements that are not valid will be excluded
    from the update. Resulting bearing values are wrapped around degrees
    range \[0, 360\]. Resulting tilt values are clamped inside degrees
    range \[0, 180\]. Resulting roll values are wrapped around degrees
    range \[-180, 180\].

    </div>

    Parameters:  
    `delta` -

    Geodetic orientation delta update.

    `origin` -

    Screen pixel origin of rotation.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="rotateBy(com.here.sdk.core.GeoOrientationUpdate)"
    class="section detail">

    ### rotateBy

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">rotateBy</span><span class="parameters">(@NonNull
    [GeoOrientationUpdate](sdk-for-android-explore-com-here-sdk-core-geoorientationupdate "class in com.here.sdk.core") delta)</span>

    </div>

    <div class="block">

    Creates an update to change map camera orientation by specified
    geodetic orientation delta. Orientation elements that are not valid
    will be excluded from the update. Resulting bearing values are
    wrapped around degrees range \[0, 360\]. Resulting tilt values are
    clamped inside degrees range \[0, 180\]. Resulting roll values are
    wrapped around degrees range \[-180, 180\].

    </div>

    Parameters:  
    `delta` -

    Geodetic orientation delta update.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="zoomBy(double,com.here.sdk.core.Point2D)"
    class="section detail">

    ### zoomBy

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">zoomBy</span><span class="parameters">(double factor,
    @NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") origin)</span>

    </div>

    <div class="block">

    Creates an update to zoom map camera by a given factor preserving a
    given focus point. Values greater than 1 zoom in map camera, by
    moving it closer to the ground; less than 1 - zoom out, which moves
    map camera further. If factor is zero, negative or not finite, no
    update will be applied to the map camera. If the focusPoint is not
    inside the viewport bounds, then the current principal point will be
    used.

    </div>

    Parameters:  
    `factor` -

    Zooming factor.

    `origin` -

    Pixel location on the screen to use as zoom origin.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="zoomTo(double)" class="section detail">

    ### zoomTo

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">zoomTo</span><span class="parameters">(double zoomLevel)</span>

    </div>

    <div class="block">

    Creates an update to move map camera's viewpoint to a particular
    zoom level by adjusting its position. If zoomLevel is not finite, no
    update will be applied to the map camera.

    </div>

    Parameters:  
    `zoomLevel` -

    The desired zoom level.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="setPrincipalPoint(com.here.sdk.core.Point2D)"
    class="section detail">

    ### setPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">setPrincipalPoint</span><span class="parameters">(@NonNull
    [Point2D](sdk-for-android-explore-com-here-sdk-core-point2d "class in com.here.sdk.core") principalPoint)</span>

    </div>

    <div class="block">

    Creates an update to change the map camera's principal point (where
    the view vector intersects the image plane - default is the center
    of the view). Point values are in screen coordinates and values that
    fall outside of the viewport, are clamped. (0,0) is top left of the
    viewport.

    </div>

    Parameters:  
    `principalPoint` -

    Principal point in absolute viewport pixel coordinates.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### setNormalizedPrincipalPoint

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">setNormalizedPrincipalPoint</span><span class="parameters">(@NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") principalPoint)</span>

    </div>

    <div class="block">

    Creates an update to change the map camera's principal point (where
    the view vector intersects the image plane - default is (0.5, 0.5)).
    Point values are in normalized screen coordinates. If the
    principalPoint is outside \[0,1\] interval, it is clamped. (0,0) is
    top left of the viewport, (1,1) is bottom right.

    </div>

    Parameters:  
    `principalPoint` -

    Principal point in normalized screen coordinates.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="setVerticalFieldOfView(double)" class="section detail">

    ### setVerticalFieldOfView

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">setVerticalFieldOfView</span><span class="parameters">(double verticalFieldOfView)</span>

    </div>

    <div class="block">

    Creates an update to change the vertical field of view of the map
    camera. If verticalFieldOfView is not finite, no update will be
    applied to the map camera. If the verticalFieldOfView is outside
    \[1, 150\] interval, it is clamped.

    </div>

    Parameters:  
    `verticalFieldOfView` -

    Vertical field of view in degrees.

    Returns:  
    MapCameraUpdate instance.

    </div>

  - <div id="compositeUpdate(java.util.List)" class="section detail">

    ### compositeUpdate

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")</span> <span class="element-name">compositeUpdate</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[MapCameraUpdate](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate "class in com.here.sdk.mapview")> mapCameraUpdates)</span>
    throws
    <span class="exceptions">[MapCameraUpdate.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a composite camera update from a list of camera updates. The
    result update will be equivalent to executing all given updates
    sequentially in the order they were provided. MapCameraAnimation
    instances derived from the MapCameraAnimationFactory and a composite
    camera update are not supported. An AnimationListener will receive
    an AnimationState.Cancelled signal when trying to apply such
    animations.

    </div>

    Parameters:  
    `mapCameraUpdates` -

    List of MapCamera updates.

    Returns:  
    MapCameraUpdate instance.

    Throws:  
    [`MapCameraUpdate.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapcameraupdate-instantiationexception "class in com.here.sdk.mapview")
    -

    Indicates an instantiation issue.

    </div>

  </div>

</div>

