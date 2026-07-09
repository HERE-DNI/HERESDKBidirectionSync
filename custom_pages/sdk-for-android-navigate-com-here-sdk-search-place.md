---
title: "Place (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-place"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Place.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.search.Place</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Place</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a location object, such as a country, a city, a point of interest (POI) etc.</p></div>
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
<section className="detail" id="serializeCompact()">
<h3>serializeCompact</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">serializeCompact</span>()</div>
<div className="block"><p>Serializes <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> to persist or transfer. Preserves limited amount of data:
 <ul>
<li><a href="sdk-for-android-navigate-com-here-sdk-search-place#getTitle()"><code>getTitle()</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-search-place#getId()"><code>getId()</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-search-place#getGeoCoordinates()"><code>getGeoCoordinates()</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-search-place#getAccessPoints()"><code>getAccessPoints()</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-search-place#getPlaceType()"><code>getPlaceType()</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-search-place#getBoundingBox()"><code>getBoundingBox()</code></a></li>
<li><a href="sdk-for-android-navigate-details#getPrimaryCategories()"><code>Details.getPrimaryCategories()</code></a></li>
<li><a href="sdk-for-android-navigate-address#addressText"><code>Address.addressText</code></a></li>
<li><a href="sdk-for-android-navigate-address#countryCode"><code>Address.countryCode</code></a></li>
</ul></p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The serialized place</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="deserialize(java.lang.String)">
<h3>deserialize</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search">Place</a></span> <span className="element-name">deserialize</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> serializedPlace)</span>
                         throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-search-placeserializationexception" title="class in com.here.sdk.search">PlaceSerializationException</a></span></div>
<div className="block"><p>Returns a <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> created from serialized string.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>serializedPlace</code> - <p>The serialized place</p></dd>
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search"><code>Place</code></a> created from serialized string.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-search-placeserializationexception" title="class in com.here.sdk.search">PlaceSerializationException</a></code> - <p>Indicates what went wrong during deserialization attempt.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTitle()">
<h3>getTitle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getTitle</span>()</div>
<div className="block"><p>Gets the localized title for the resource.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The localized title for the resource.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getId()">
<h3>getId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getId</span>()</div>
<div className="block"><p>Gets the unique id of this resource. It can be used to query further information.
 When returned from <code>OfflineSearchEngine</code>, <code>id</code> is valid only for <code>Place</code> objects whose
 <code>place_type</code> is <code>POI</code>. Otherwise, it is empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The unique id of this resource. It can be used to query further information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPlaceType()">
<h3>getPlaceType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-placetype" title="enum class in com.here.sdk.search">PlaceType</a></span> <span className="element-name">getPlaceType</span>()</div>
<div className="block"><p>Gets the place type.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The place type.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAreaType()">
<h3>getAreaType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-areatype" title="enum class in com.here.sdk.search">AreaType</a></span> <span className="element-name">getAreaType</span>()</div>
<div className="block"><p>Gets the area type. It is available only when the <a href="sdk-for-android-navigate-com-here-sdk-search-place#getPlaceType()"><code>getPlaceType()</code></a> is <a href="sdk-for-android-navigate-placetype#AREA"><code>PlaceType.AREA</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The area type. It is available only when the <a href="sdk-for-android-navigate-com-here-sdk-search-place#getPlaceType()"><code>getPlaceType()</code></a> is <a href="sdk-for-android-navigate-placetype#AREA"><code>PlaceType.AREA</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAddress()">
<h3>getAddress</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-address" title="class in com.here.sdk.search">Address</a></span> <span className="element-name">getAddress</span>()</div>
<div className="block"><p>Gets the address of the place.
 Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
 <code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <a href="sdk-for-android-navigate-address#addressText"><code>Address.addressText</code></a>.
 Complete address details can be obtained by searching with <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The address of the place.
     Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
     <code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <a href="sdk-for-android-navigate-address#addressText"><code>Address.addressText</code></a>.
     Complete address details can be obtained by searching with <a href="sdk-for-android-navigate-com-here-sdk-search-placeidquery" title="class in com.here.sdk.search"><code>PlaceIdQuery</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDetails()">
<h3>getDetails</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-details" title="class in com.here.sdk.search">Details</a></span> <span className="element-name">getDetails</span>()</div>
<div className="block"><p>Gets the place's detailed information.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The place's detailed information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeoCoordinates()">
<h3>getGeoCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getGeoCoordinates</span>()</div>
<div className="block"><p>Gets the geographic coordinates of the place.
 Can be <code>null</code> when retrieved from a suggestion's place property.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the place.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isCoordinatesInterpolated()">
<h3>isCoordinatesInterpolated</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isCoordinatesInterpolated</span>()</div>
<div className="block"><p>Gets the flag saying whether the coordinates of the house number were interpolated or not.
 This property is valid only for house number results retrieved using online search.
 When false, it means <a href="sdk-for-android-navigate-com-here-sdk-search-place#getGeoCoordinates()"><code>getGeoCoordinates()</code></a> point to an accurate position of the house. Otherwise
 coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A property that says whether the coordinates of the house number were interpolated or not.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAccessPoints()">
<h3>getAccessPoints</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span className="element-name">getAccessPoints</span>()</div>
<div className="block"><p>Gets the access points to the place, such as the points on a road or in a parking lot.
 A place can have multiple access points. For example, a large warehouse can have
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
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The access points to the place, such as the points on a road or in a parking lot.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets the geographic coordinates of the bounding box containing the place.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the map bounding box containing the place.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDistanceInMeters()">
<h3>getDistanceInMeters</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">getDistanceInMeters</span>()</div>
<div className="block"><p>Gets the distance from the search center to the place in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The distance from the search center to the place in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPoliticalView()">
<h3>getPoliticalView</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getPoliticalView</span>()</div>
<div className="block"><p>Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.
 Populated when the geopolitical view parameter is set in the <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>
 and passed to <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> on instantiation,
 but only if it is an alternative view.
 For more details refer to <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>
