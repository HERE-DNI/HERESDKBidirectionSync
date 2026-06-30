---
title: "LocationIndicator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-locationindicator"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationIndicator.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.LocationIndicator</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LocationIndicator</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Graphical object to represent the location of the user on the map.
 It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style.
 This style can be changed by <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)"><code>setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)</code></a>
The location is made available to an instance of this class by calling <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#updateLocation(com.here.sdk.core.Location)"><code>updateLocation(Location)</code></a> or
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#updateLocation(com.here.sdk.core.Location,com.here.sdk.mapview.MapCameraUpdate)"><code>updateLocation(Location, MapCameraUpdate)</code></a>.
 Use <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#enable(com.here.sdk.mapview.MapViewBase)"><code>enable(com.here.sdk.mapview.MapViewBase)</code></a> to add this object to the map and <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#disable()"><code>disable()</code></a> to remove it.
 Take care that the
 location indicator is not accidentally added to the map view multiple times for example when the
 android activity is recreated after an orientation change.
 Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera
 to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the
 MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly
 disappear from the viewport due to the new perspective.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a></code></div>
<div class="col-last even-row-color">
<div class="block">The predefined styles for the location indicator which are pedestrian and navigation mode.</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-markertype" title="enum class in com.here.sdk.mapview">LocationIndicator.MarkerType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Enum to identify different types of markers of the location indicator.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#%3Cinit%3E()">LocationIndicator</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of LocationIndicator.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#%3Cinit%3E(com.here.sdk.mapview.MapViewBase)">LocationIndicator</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance of LocationIndicator and adds it to provided <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#disable()">disable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This function removes <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> from map view.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#enable(com.here.sdk.mapview.MapViewBase)">enable</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> for provided <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#getHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)">getHaloColor</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#getLocationIndicatorStyle()">getLocationIndicatorStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns visual style of location indicator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-materialreflectivity" title="class in com.here.sdk.mapview">MaterialReflectivity</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#getMaterialReflectivity()">getMaterialReflectivity</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves the material reflectivity applied to all markers of location indicator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#getOpacity()">getOpacity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current opacity of the location indicator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#isAccuracyVisualized()">isAccuracyVisualized</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> is used to scale the accuracy indicator halo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#isActive()">isActive</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <code>true</code> if active version of the location indicator is shown or <code>false</code>
 when inactive version is shown.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setAccuracyVisualized(boolean)">setAccuracyVisualized</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> is used to scale the accuracy indicator halo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setActive(boolean)">setActive</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether the active or inactive version of location indicator is to be shown.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle,com.here.sdk.core.Color)">setHaloColor</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a> style,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the color of the accuracy indicator halo for a given style.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)">setLocationIndicatorStyle</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the visual style of location indicator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType)">setMarker3dModel</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-markertype" title="enum class in com.here.sdk.mapview">LocationIndicator.MarkerType</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType,com.here.sdk.mapview.RenderSize.Unit)">setMarker3dModel</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-markertype" title="enum class in com.here.sdk.mapview">LocationIndicator.MarkerType</a> type,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> renderSizeUnit)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a> asset to be displayed as location indicator for a specified type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setMaterialReflectivity(com.here.sdk.mapview.MaterialReflectivity)">setMaterialReflectivity</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-materialreflectivity" title="class in com.here.sdk.mapview">MaterialReflectivity</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the material reflectivity properties for all markers of location indicator including its halo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#setOpacity(double)">setOpacity</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the opacity of the location indicator.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#updateLocation(com.here.sdk.core.Location)">updateLocation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates the indicator to a new location.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#updateLocation(com.here.sdk.core.Location,com.here.sdk.mapview.MapCameraUpdate)">updateLocation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates the indicator to a new location and applies a camera update at the same time.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>LocationIndicator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationIndicator</span>()</div>
<div class="block"><p>Creates an instance of LocationIndicator.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapViewBase)">
<h3>LocationIndicator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationIndicator</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div class="block"><p>Creates an instance of LocationIndicator and adds it to provided <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a> instance.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="enable(com.here.sdk.mapview.MapViewBase)">
<h3>enable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enable</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div class="block"><p>Enables <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> for provided <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a>.
 If <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> is already enabled (added to map view) for passed map view, this function does nothing.
 If <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> is added to different <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a>, this function removes first <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a>
 from previous map view before adding to new one.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapView</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview"><code>MapViewBase</code></a> instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disable()">
<h3>disable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disable</span>()</div>
<div class="block"><p>This function removes <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> from map view.
 If <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator" title="class in com.here.sdk.mapview"><code>LocationIndicator</code></a> was not added to any map view yet, this function does nothing.</p></div>
</section>
</li>
<li>
<section class="detail" id="updateLocation(com.here.sdk.core.Location)">
<h3>updateLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLocation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Updates the indicator to a new location.
 If accuracy visualized is set to <code>true</code> the field <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a>
 determines the size of the accuracy indicator halo.
 The altitude of the location is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - <p>The updated location of the user.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateLocation(com.here.sdk.core.Location,com.here.sdk.mapview.MapCameraUpdate)">
<h3>updateLocation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateLocation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a> cameraUpdate)</span></div>
<div class="block"><p>Updates the indicator to a new location and applies a camera update at the same time.
 Does nothing if the indicator instance is not enabled.
 If accuracy visualized is set to <code>true</code> the field <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a>
 determines the size of the accuracy indicator halo.
 The altitude of the location is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - <p>The updated location of the user.</p></dd>
<dd><code>cameraUpdate</code> - <p>The update to apply to the camera.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType)">
<h3>setMarker3dModel</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMarker3dModel</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-markertype" title="enum class in com.here.sdk.mapview">LocationIndicator.MarkerType</a> type)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0. Please use the overloaded method with <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> instead.</p></div>
</div>
<div class="block"><p>Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.
 The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
 z axis is the depth. The direction in which the location indicator is pointing is the
 positive z axis. Please note that only MapMarker3DModel created from *.obj files are
 supported. Models created from Mesh will be ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>model</code> - <p>The MapMarker3DModel object to be displayed for the specified type. Only models
     created from obj files are supported. Those created from mesh will be ignored.</p></dd>
<dd><code>scale</code> - <p>The scaling which will be applied to the marker model. As the size of the
     location marker should be aligned on devices with different resolutions the
     scale factor is applied relative to the ppi value and thus differs from the
     scale which is passed to <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a> objects.
     Meter is used for the unit of the map marker 3d model coordinate system.
     For historical reason, the scale factor is internally devided by 6.
     To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p></dd>
<dd><code>type</code> - <p>The type of location marker for which the marker 3d model should be replaced.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType,com.here.sdk.mapview.RenderSize.Unit)">
<h3>setMarker3dModel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMarker3dModel</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview">MapMarker3DModel</a> model,
 double scale,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-markertype" title="enum class in com.here.sdk.mapview">LocationIndicator.MarkerType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> renderSizeUnit)</span></div>
<div class="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a> asset to be displayed as location indicator for a specified type.
 The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
 z axis is the depth. The direction in which the location indicator is pointing is the
 positive z axis. Please note that only <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a> created from <code>obj</code> files are
 supported. Models created from Mesh will be ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>model</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3dmodel" title="class in com.here.sdk.mapview"><code>MapMarker3DModel</code></a> object to be displayed for the specified type. Only models
     created from <code>obj</code> files are supported. Those created from mesh will be ignored.</p></dd>
<dd><code>scale</code> - <p>A scale factor applied to the marker model.</p></dd>
<dd><code>type</code> - <p>The type of location marker for which the marker 3d model should be replaced.</p></dd>
<dd><code>renderSizeUnit</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> specifying how the vertex coordinates of the
     3D model are being interpreted. It specifies whether the 3D model is placed in world or
     screen coordinate space.
     <a href="sdk-for-android-navigate-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> will make the 3D model use world
     coordinate space, meaning that it will change size together with the map
     when it is zoomed in and out. A simple 10 by 10 by 10 (in model space) cube
     will have a size of 10 by 10 by 10 meters in world space.
     <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> makes the 3D model use screen coordinate space,
     meaning that it will have constant size on the screen regardless
     of how the map zoom changes. A simple 10 by 10 (in model space) rectangle
     will have a size of 10 by 10 pixels on the screen.
     <a href="sdk-for-android-navigate-rendersize-unit#DENSITY_INDEPENDENT_PIXELS"><code>RenderSize.Unit.DENSITY_INDEPENDENT_PIXELS</code></a> is similar to pixels,
     but the resulting size will take into account the pixel density of the
     display, meaning that physical size on the screen will be approximately
     the same regardless of the size or resolution of the display.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle,com.here.sdk.core.Color)">
<h3>setHaloColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHaloColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a> style,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span></div>
<div class="block"><p>Sets the color of the accuracy indicator halo for a given style.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - <p>The type of IndicatorStyle for which the color should be assigned.</p></dd>
<dd><code>color</code> - <p>The color to be applied to the halo for a specified IndicatorStyle.
     Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
     Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHaloColor(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)">
<h3>getHaloColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getHaloColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a> style)</span></div>
<div class="block"><p>Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.
 The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - <p>The type of IndicatorStyle for which the color should be returned.</p></dd>
<dt>Returns:</dt>
<dd><p>The color of the halo for the specified IndicatorStyle.
     Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
     Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAccuracyVisualized()">
<h3>isAccuracyVisualized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAccuracyVisualized</span>()</div>
<div class="block"><p>Returns whether <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> is used to scale the accuracy indicator halo.
 Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAccuracyVisualized(boolean)">
<h3>setAccuracyVisualized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAccuracyVisualized</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> is used to scale the accuracy indicator halo.
 Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.
 When set to <code>true</code>, the radius of the halo corresponds to the value of
 <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> passed to <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#updateLocation(com.here.sdk.core.Location)"><code>updateLocation(Location)</code></a>
 and scales in world coordinates.
 For values smaller than 20 meters the halo is hidden.
 The radius of the halo is limited to 500 meters and values higher than that or <code>null</code>
 will keep the halo at that size.
 If the location indicator is set to inactive (which can be checked via <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator#isActive()"><code>isActive()</code></a> flag),
 then the halo is always hidden. The value of this property remains unchanged regardless of the flag's value.
 If the location indicator is set to active:
 <ul>
<li>Built-in location indicators:
 <ul>
<li>The halo is always shown.</li>
<li>If the accuracy visualization is set to <code>true</code>, the size of the halo scales with
 <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, halo displays at a default size.</li>
</ul>
</li>
<li>Custom location indicator:
 <ul>
<li>If the accuracy visualization is set to <code>true</code>, halo is shown and the size of the halo scales with
 <a href="sdk-for-android-navigate-location#horizontalAccuracyInMeters"><code>Location.horizontalAccuracyInMeters</code></a> in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, no halo is shown since it might not fit together with the custom 3d model.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocationIndicatorStyle()">
<h3>getLocationIndicatorStyle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a></span> <span class="element-name">getLocationIndicatorStyle</span>()</div>
<div class="block"><p>Returns visual style of location indicator.
 By default, it is set to <a href="sdk-for-android-navigate-locationindicator-indicatorstyle#NAVIGATION"><code>LocationIndicator.IndicatorStyle.NAVIGATION</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The visual style of location indicator.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLocationIndicatorStyle(com.here.sdk.mapview.LocationIndicator.IndicatorStyle)">
<h3>setLocationIndicatorStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLocationIndicatorStyle</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-locationindicator-indicatorstyle" title="enum class in com.here.sdk.mapview">LocationIndicator.IndicatorStyle</a> value)</span></div>
<div class="block"><p>Sets the visual style of location indicator.
 By default, it is set to <a href="sdk-for-android-navigate-locationindicator-indicatorstyle#NAVIGATION"><code>LocationIndicator.IndicatorStyle.NAVIGATION</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The visual style of location indicator.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isActive()">
<h3>isActive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isActive</span>()</div>
<div class="block"><p>Returns <code>true</code> if active version of the location indicator is shown or <code>false</code>
 when inactive version is shown. By default, it is <code>true</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A Boolean value that determines whether the active on inactive version of location indicator is shown.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setActive(boolean)">
<h3>setActive</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setActive</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether the active or inactive version of location indicator is to be shown.
 the indicator to active state if <code>true</code> is passed and to inactive state when false
 is passed. By default, it is <code>true</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A Boolean value that determines whether the active on inactive version of location indicator is shown.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpacity()">
<h3>getOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()</div>
<div class="block"><p>Gets the current opacity of the location indicator.
 Default value is 1.0 which means location
 indicator is displayed with the default alpha channel of the texture.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOpacity(double)">
<h3>setOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the opacity of the location indicator.
 Provided value is clamped in range [0.0, 1.0].
 Default value is 1.0 which means location
 indicator is displayed with the default alpha channel of the texture.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The factor applied to the alpha channel of both the location indicator's texture and the accuracy indicator's halo color.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMaterialReflectivity()">
<h3>getMaterialReflectivity</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-materialreflectivity" title="class in com.here.sdk.mapview">MaterialReflectivity</a></span> <span class="element-name">getMaterialReflectivity</span>()</div>
<div class="block"><p>Retrieves the material reflectivity applied to all markers of location indicator.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
 Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
 inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
 markers are shaded by scene lights using the provided ambient / diffuse factors. When set
 back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.
 Default value is <code>null</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The material reflectivity properties of the location indicator.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMaterialReflectivity(com.here.sdk.mapview.MaterialReflectivity)">
<h3>setMaterialReflectivity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMaterialReflectivity</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-materialreflectivity" title="class in com.here.sdk.mapview">MaterialReflectivity</a> value)</span></div>
<div class="block"><p>Sets the material reflectivity properties for all markers of location indicator including its halo.
 This value affects also any custom markers set with <code>setMarker3dModel</code>.
 Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
 inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
 markers are shaded by scene lights using the provided ambient / diffuse factors. When set
 back to <code>null</code>, lighting is disabled and markers revert to unlit (emissive) rendering.
 Default value is <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The material reflectivity properties of the location indicator.</p></dd>
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
