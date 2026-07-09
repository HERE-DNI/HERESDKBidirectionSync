---
title: "MapCameraUpdateFactory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdatefactory"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapCameraUpdateFactory.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapCameraUpdateFactory</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapCameraUpdateFactory</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Factory for creating MapCameraUpdate to change map's camera.
 For some factory methods you can apply an additional padding in pixels by setting a
 <code>viewRectangle</code> parameter based on the current size of the map view:
 <pre><code>int leftPaddingInPixels = 5;
 int rightPaddingInPixels = 5;
 int topPaddingInPixels = 5;
 int bottomPaddingInPixels = 5;
 int horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
 int verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels;

 Point2D origin = new Point2D(leftPaddingInPixels, topPaddingInPixels);
 Size2D sizeInPixels = new Size2D(mapView.getWidth() - horizontalPaddingInPixels, mapView.getHeight() - verticalPaddingInPixels);
 Rectangle2D paddedViewRectangle = new Rectangle2D(origin, sizeInPixels);
 </code></pre>
The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates
 also the top-left corner of the map's viewport.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target)</span></div>
<div className="block"><p>Creates an update to position the map camera to look at the given target,
 preserving the current orientation at look-at target and map measure.
 Any target sub-element value that is not finite will be excluded from the update.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates, altitude is ignored,
     the target is considered to be located on the ground.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation)</span></div>
<div className="block"><p>Creates an update to position the map camera to look at the given target with the given
 orientation preserving the current map measure (zoom level/distance/scale)
 Any target or orientation sub-element value that is not finite will be excluded from the update.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</span></div>
<div className="block"><p>Creates an update to position the map camera to look at the given target with the given
 map measure preserving the current orientation at look-at target.
 Any target sub-element value that is not finite will be excluded from the update.
 If the map measure is not valid, the current map camera distance to the target point is preserved.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>measure</code> - <p>The desired map measure.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</span></div>
<div className="block"><p>Creates an update to position the map camera to look at the given target with the given
 orientation and map measure.
 Any target or orientation sub-element value that is not finite will be excluded from the update.
 If the map measure is not valid, the current map camera distance to the target point is preserved.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dd><code>measure</code> - <p>The desired map measure.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookToMatch</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookToMatch</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoPoint,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewPoint,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</span></div>
<div className="block"><p>Creates an update to position the map camera to look at the map with the given
 orientation and map measure and with the given geo point located at the given view point.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.
 Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoPoint</code> - <p>The geo point that will be matched to the given view point.
     Note: the geo point will differ from the look at target of the camera. After this update the camera
     will still look at the principal point and therefore the look at target will be different from the geo
     point, since the geo point will correspond to the given view point and the look at target
     will correspond to the principal point. Look at target and the geo point will be identical only
     if the given view point is identical to the principal point.</p></dd>
<dd><code>viewPoint</code> - <p>View point coordinates in pixels.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dd><code>measure</code> - <p>The desired map measure.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D)">
<h3>lookToMatch</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookToMatch</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoPoint,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewPoint)</span></div>
<div className="block"><p>Creates an update to position the map camera to look at the map
 with the given geo point located at the given view point.
 Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
 The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoPoint</code> - <p>The geo point that will be matched to the given view point.
     Note: the geo point will differ from the look at target of the camera. After this update the camera
     will still look at the principal point and therefore the look at target will be different from the geo
     point, since the geo point will correspond to the given view point and the look at target
     will correspond to the principal point. Look at target and the geo point will be identical only
     if the given view point is identical to the principal point.</p></dd>
<dd><code>viewPoint</code> - <p>View point coordinates in pixels.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measureLimit)</span></div>
<div className="block"><p>Create an update to look at the given geo locations and fit them inside the given rectangle,
 in accordance with a map measure limit.
 If the provided <code>points</code> list is empty, no update will be applied to the camera.
 If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 All <code>viewRectangle</code> values need to be finite to be considered as valid.
 If measure limit is not valid, no update will be applied to the map camera.
 The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - <p>Array of points in geodetic space that should be visible inside the given view rectangle.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at the new calculated target point.</p></dd>
<dd><code>measureLimit</code> - <p>Map measure limit:
     <ul>
<li>as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters.
     The map camera should not be positioned closer to the center of view rectangle than this.</li>
<li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for
     the calculated lookAt target point. Can be used to not zoom closer than a given level.</li>
<li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the center of view rectangle in meters. This is not the scale for
     the calculated lookAt target point.</li>
</ul></p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapMeasure,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> minMeasure,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> maxMeasure)</span></div>
<div className="block"><p>Creates an update to position the camera to look at the given target with the given
 orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.
 Such position update can possibly not be found.
 Any target or orientation sub-element value that is not finite will be excluded from the update.
 If the provided <code>points</code> list is empty, no update will be applied to the map camera.
 If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 If map measures are not valid, no update will be applied to the map camera.
 The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dd><code>points</code> - <p>Array of points in geodetic space that should be visible inside the given view rectangle.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates inside which the geographical points are displayed.</p></dd>
<dd><code>minMeasure</code> - <p>Minimum map measure:
     <ul>
<li>as distance: the minimum distance from map camera to earth surface at the look-at target in meters.
     The map camera should not be positioned closer to target than this.</li>
<li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.
     Can be used to not zoom closer than a given level.</li>
<li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.</li>
</ul></p></dd>
<dd><code>maxMeasure</code> - <p>Maximum map measure:
     <ul>
<li>as distance: the maximum distance from map camera to earth surface at the look-at target in meters.
     The map camera should not be positioned further from target than this.</li>
<li>as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.
     Can be used to not zoom further than a given level.</li>
<li>as scale: the maximum scale for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.</li>
</ul></p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</span></div>
<div className="block"><p>Create an update to look at the given geo-box and fit it inside the given rectangle.
 If geoBox is not valid, no update will be applied to the map camera.
 If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 All <code>viewRectangle</code> values need to be finite to be considered as valid.
 In cases where it is not possible to find a solution for the given parameters,
 the resulting MapCameraUpdate will not change the map camera.
 The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic box that should be visible inside the given view rectangle.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at the target point.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.Rectangle2D)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</span></div>
<div className="block"><p>Creates an update to look at the given geo-box and fit it inside the given rectangle,
 preserving current orientation and zooming at the center of view rectangle.
 If geoBox is not valid, no update will be applied to the map camera.
 If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 In cases where it is not possible to find a solution for the given parameters,
 the resulting MapCameraUpdate will not change the map camera.
 The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic box that should be visible inside the given view rectangle.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookAt(com.here.sdk.core.GeoBox)">
<h3>lookAt</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">lookAt</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target)</span></div>
<div className="block"><p>Creates an update to look at the given geo-box,
 preserving current orientation and zooming at the center of viewport.
 If geoBox is not valid, no update will be applied to the map camera.
 The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic box that should be visible inside the viewport rectangle.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="panBy(double,double)">
<h3>panBy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">panBy</span><wbr/><span className="parameters">(double xOffset,
 double yOffset)</span></div>
<div className="block"><p>Creates an update to pan map camera over the map by the specified number of pixels
 in the x and y direction starting from current principal point position.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>xOffset</code> - <p>X offset in pixels</p></dd>
<dd><code>yOffset</code> - <p>Y offset in pixels</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D)">
<h3>orbitBy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">orbitBy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</span></div>
<div className="block"><p>Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.
 If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.
 Orientation elements that are not valid will be excluded from the update.
 Resulting bearing values are wrapped around degrees range [0, 360].
 Resulting tilt values are clamped inside degrees range [0, 180].
 Resulting roll values are wrapped around degrees range [-180, 180].</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>delta</code> - <p>Geodetic orientation delta update.</p></dd>
<dd><code>origin</code> - <p>Screen pixel origin of rotation.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="rotateBy(com.here.sdk.core.GeoOrientationUpdate)">
<h3>rotateBy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">rotateBy</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta)</span></div>
<div className="block"><p>Creates an update to change map camera orientation by specified geodetic orientation delta.
 Orientation elements that are not valid will be excluded from the update.
 Resulting bearing values are wrapped around degrees range [0, 360].
 Resulting tilt values are clamped inside degrees range [0, 180].
 Resulting roll values are wrapped around degrees range [-180, 180].</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>delta</code> - <p>Geodetic orientation delta update.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="zoomBy(double,com.here.sdk.core.Point2D)">
<h3>zoomBy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">zoomBy</span><wbr/><span className="parameters">(double factor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</span></div>
<div className="block"><p>Creates an update to zoom map camera by a given factor preserving a given focus point.
 Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out,
 which moves map camera further.
 If factor is zero, negative or not finite, no update will be applied to the map camera.
 If the focusPoint is not inside the viewport bounds, then the current principal point will be used.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>factor</code> - <p>Zooming factor.</p></dd>
<dd><code>origin</code> - <p>Pixel location on the screen to use as zoom origin.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="zoomTo(double)">
<h3>zoomTo</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">zoomTo</span><wbr/><span className="parameters">(double zoomLevel)</span></div>
<div className="block"><p>Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.
 If zoomLevel is not finite, no update will be applied to the map camera.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>zoomLevel</code> - <p>The desired zoom level.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setPrincipalPoint(com.here.sdk.core.Point2D)">
<h3>setPrincipalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">setPrincipalPoint</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> principalPoint)</span></div>
<div className="block"><p>Creates an update to change the map camera's principal point (where the view vector intersects
 the image plane - default is the center of the view). Point values are in screen coordinates
 and values that fall outside of the viewport, are clamped.
 (0,0) is top left of the viewport.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>principalPoint</code> - <p>Principal point in absolute viewport pixel coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">
<h3>setNormalizedPrincipalPoint</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">setNormalizedPrincipalPoint</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> principalPoint)</span></div>
<div className="block"><p>Creates an update to change the map camera's principal point (where the view vector
 intersects the image plane - default is (0.5, 0.5)). Point values are in normalized screen coordinates.
 If the principalPoint is outside [0,1] interval, it is clamped.
 (0,0) is top left of the viewport, (1,1) is bottom right.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>principalPoint</code> - <p>Principal point in normalized screen coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setVerticalFieldOfView(double)">
<h3>setVerticalFieldOfView</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">setVerticalFieldOfView</span><wbr/><span className="parameters">(double verticalFieldOfView)</span></div>
<div className="block"><p>Creates an update to change the vertical field of view of the map camera.
 If verticalFieldOfView is not finite, no update will be applied to the map camera.
 If the verticalFieldOfView is outside [1, 150] interval, it is clamped.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>verticalFieldOfView</code> - <p>Vertical field of view in degrees.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="compositeUpdate(java.util.List)">
<h3>compositeUpdate</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span className="element-name">compositeUpdate</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a>&gt; mapCameraUpdates)</span>
                                       throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate-instantiationexception" title="class in com.here.sdk.mapview">MapCameraUpdate.InstantiationException</a></span></div>
<div className="block"><p>Creates a composite camera update from a list of camera updates. The result update will be
 equivalent to executing all given updates sequentially in the order they were provided.
 MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera
 update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal
 when trying to apply such animations.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapCameraUpdates</code> - <p>List of MapCamera updates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate-instantiationexception" title="class in com.here.sdk.mapview">MapCameraUpdate.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
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
