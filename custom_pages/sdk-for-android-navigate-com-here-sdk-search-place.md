---
title: "Place (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-place"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Place.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.search.Place</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Place</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a location object, such as a country, a city, a point of interest (POI) etc.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search">Place</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#deserialize(java.lang.String)">deserialize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> serializedPlace)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> created from serialized string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getAccessPoints()">getAccessPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the access points to the place, such as the points on a road or in a parking lot.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-address" title="class in com.here.sdk.search">Address</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getAddress()">getAddress</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the address of the place.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-areatype" title="enum class in com.here.sdk.search">AreaType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getAreaType()">getAreaType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the area type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geographic coordinates of the bounding box containing the place.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-details" title="class in com.here.sdk.search">Details</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDetails()">getDetails</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the place's detailed information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getDistanceInMeters()">getDistanceInMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the distance from the search center to the place in meters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getGeoCoordinates()">getGeoCoordinates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geographic coordinates of the place.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getId()">getId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the unique id of this resource.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-placetype" title="enum class in com.here.sdk.search">PlaceType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPlaceType()">getPlaceType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the place type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPoliticalView()">getPoliticalView</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTitle()">getTitle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the localized title for the resource.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#isCoordinatesInterpolated()">isCoordinatesInterpolated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the flag saying whether the coordinates of the house number were interpolated or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#serializeCompact()">serializeCompact</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Serializes <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> to persist or transfer.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="serializeCompact()">
<h3>serializeCompact</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">serializeCompact</span>()</div>
<div class="block"><p>Serializes <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> to persist or transfer. Preserves limited amount of data:
 <ul>
<li><a href="sdk-for-android-navigate-index#getTitle()"><code>getTitle()</code></a></li>
<li><a href="sdk-for-android-navigate-index#getId()"><code>getId()</code></a></li>
<li><a href="sdk-for-android-navigate-index#getGeoCoordinates()"><code>getGeoCoordinates()</code></a></li>
<li><a href="sdk-for-android-navigate-index#getAccessPoints()"><code>getAccessPoints()</code></a></li>
<li><a href="sdk-for-android-navigate-index#getPlaceType()"><code>getPlaceType()</code></a></li>
<li><a href="sdk-for-android-navigate-index#getBoundingBox()"><code>getBoundingBox()</code></a></li>
<li><a href="sdk-for-android-navigate-details#getPrimaryCategories()"><code>Details.getPrimaryCategories()</code></a></li>
<li><a href="sdk-for-android-navigate-address#addressText"><code>Address.addressText</code></a></li>
<li><a href="sdk-for-android-navigate-address#countryCode"><code>Address.countryCode</code></a></li>
</ul></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The serialized place</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deserialize(java.lang.String)">
<h3>deserialize</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search">Place</a></span> <span class="element-name">deserialize</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> serializedPlace)</span>
                         throws <span class="exceptions"><a href="sdk-for-android-navigate-placeserializationexception" title="class in com.here.sdk.search">PlaceSerializationException</a></span></div>
<div class="block"><p>Returns a <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> created from serialized string.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>serializedPlace</code> - <p>The serialized place</p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-place" title="class in com.here.sdk.search"><code>Place</code></a> created from serialized string.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-placeserializationexception" title="class in com.here.sdk.search">PlaceSerializationException</a></code> - <p>Indicates what went wrong during deserialization attempt.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<div class="block"><p>Gets the localized title for the resource.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The localized title for the resource.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block"><p>Gets the unique id of this resource. It can be used to query further information.
 </p><p>When returned from <code>OfflineSearchEngine</code>, <code>id</code> is valid only for <code>Place</code> objects whose
 <code>place_type</code> is <code>POI</code>. Otherwise, it is empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The unique id of this resource. It can be used to query further information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPlaceType()">
<h3>getPlaceType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-placetype" title="enum class in com.here.sdk.search">PlaceType</a></span> <span class="element-name">getPlaceType</span>()</div>
<div class="block"><p>Gets the place type.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The place type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAreaType()">
<h3>getAreaType</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-areatype" title="enum class in com.here.sdk.search">AreaType</a></span> <span class="element-name">getAreaType</span>()</div>
<div class="block"><p>Gets the area type. It is available only when the <a href="sdk-for-android-navigate-index#getPlaceType()"><code>getPlaceType()</code></a> is <a href="sdk-for-android-navigate-placetype#AREA"><code>PlaceType.AREA</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The area type. It is available only when the <a href="sdk-for-android-navigate-index#getPlaceType()"><code>getPlaceType()</code></a> is <a href="sdk-for-android-navigate-placetype#AREA"><code>PlaceType.AREA</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAddress()">
<h3>getAddress</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-address" title="class in com.here.sdk.search">Address</a></span> <span class="element-name">getAddress</span>()</div>
<div class="block"><p>Gets the address of the place.
 </p><p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
 <code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <a href="sdk-for-android-navigate-address#addressText"><code>Address.addressText</code></a>.
 Complete address details can be obtained by searching with <a href="sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The address of the place.
     </p><p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
     <code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <a href="sdk-for-android-navigate-address#addressText"><code>Address.addressText</code></a>.
     Complete address details can be obtained by searching with <a href="sdk-for-android-navigate-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDetails()">
<h3>getDetails</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-details" title="class in com.here.sdk.search">Details</a></span> <span class="element-name">getDetails</span>()</div>
<div class="block"><p>Gets the place's detailed information.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The place's detailed information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeoCoordinates()">
<h3>getGeoCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getGeoCoordinates</span>()</div>
<div class="block"><p>Gets the geographic coordinates of the place.
 </p><p>Can be <code>null</code> when retrieved from a suggestion's place property.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the place.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCoordinatesInterpolated()">
<h3>isCoordinatesInterpolated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCoordinatesInterpolated</span>()</div>
<div class="block"><p>Gets the flag saying whether the coordinates of the house number were interpolated or not.
 </p><p>This property is valid only for house number results retrieved using online search.
 When false, it means <a href="sdk-for-android-navigate-index#getGeoCoordinates()"><code>getGeoCoordinates()</code></a> point to an accurate position of the house. Otherwise
 coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A property that says whether the coordinates of the house number were interpolated or not.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAccessPoints()">
<h3>getAccessPoints</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span class="element-name">getAccessPoints</span>()</div>
<div class="block"><p>Gets the access points to the place, such as the points on a road or in a parking lot.
 </p><p>A place can have multiple access points. For example, a large warehouse can have
 multiple entrances, while the center of the warehouse may not be directly reachable.
 Note that access points are meant to be reachable by vehicles.
 For routes it is recommended to navigate to one of the available access points (if any),
 whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
 The list is empty when no access points are known or when the place is directly reachable.
 A place can have multiple access points. For example, a large warehouse can have
 multiple entrances, while the center of the warehouse may not be directly reachable.
 Note that access points are meant to be reachable by vehicles.
 For routes it is recommended to navigate to one of the available access points (if any),
 whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
 The list is empty when no access points are known or when the place is directly reachable.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The access points to the place, such as the points on a road or in a parking lot.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getBoundingBox</span>()</div>
<div class="block"><p>Gets the geographic coordinates of the bounding box containing the place.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the map bounding box containing the place.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDistanceInMeters()">
<h3>getDistanceInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">getDistanceInMeters</span>()</div>
<div class="block"><p>Gets the distance from the search center to the place in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The distance from the search center to the place in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPoliticalView()">
<h3>getPoliticalView</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPoliticalView</span>()</div>
<div class="block"><p>Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.
 </p><p>Populated when the geopolitical view parameter is set in the <a href="sdk-for-android-navigate-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>
 and passed to <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> on instantiation,
 but only if it is an alternative view.
 For more details refer to <a href="sdk-for-android-navigate-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.</p></dd>
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
`
}</HTMLBlock>
