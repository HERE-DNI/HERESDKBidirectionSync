---
title: "PhysicalAttributes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PhysicalAttributes.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapdata.PhysicalAttributes</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PhysicalAttributes</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Physical attributes of the segment.
 </p><p><em><strong>Note</strong></em> a road can have more than one attribute at the same time.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-roaddivider" title="enum class in com.here.sdk.mapdata">RoadDivider</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#divider">divider</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the presence of a road divider.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isBoatFerry">isBoatFerry</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identifies a generalised route of a boat ferry for passengers or vehicles over water.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isBridge">isBridge</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isDirtRoad">isDirtRoad</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates whether the navigable segment is paved.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isMultiplyDigitized">isMultiplyDigitized</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies separately digitised roads, i.e., roads that are digitised with one line per
 direction of traffic instead of one line per road.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isPrivate">isPrivate</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isRailFerry">isRailFerry</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies a generalised route of a ferry for passengers or vehicles via rail.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isRoundabout">isRoundabout</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the presence of a roundabout.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isTunnel">isTunnel</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies an enclosed (on all sides) passageway through or under an obstruction.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#%3Cinit%3E()">PhysicalAttributes</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance with default values.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="isDirtRoad">
<h3>isDirtRoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirtRoad</span></div>
<div class="block"><p>Indicates whether the navigable segment is paved.
 Paved is primarily used for map display and routing by assigning
 higher penalties to unpaved roads.
 Paved roads are made of concrete, asphalt, cobblestone or brick.
 Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTunnel">
<h3>isTunnel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTunnel</span></div>
<div class="block"><p>Identifies an enclosed (on all sides) passageway through or under an obstruction.
 This attribute can be used for display or route guidance.</p></div>
</section>
</li>
<li>
<section class="detail" id="isBridge">
<h3>isBridge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBridge</span></div>
<div class="block"><p>Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.
 Bridge is published on segments that represent significant
 bridges and/or overpasses; elevated roads are not published as bridge.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPrivate">
<h3>isPrivate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrivate</span></div>
<div class="block"><p>Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.
 Allows for unique cartographic representation of roads that restrict public use.
 May be used to avoid routing through a private road.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRoundabout">
<h3>isRoundabout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRoundabout</span></div>
<div class="block"><p>Indicates the presence of a roundabout.</p></div>
</section>
</li>
<li>
<section class="detail" id="isMultiplyDigitized">
<h3>isMultiplyDigitized</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMultiplyDigitized</span></div>
<div class="block"><p>Identifies separately digitised roads, i.e., roads that are digitised with one line per
 direction of traffic instead of one line per road.
 It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus
 lane) are located between the separately digitised opposing roadbeds if driver perception
 remains unchanged.</p></div>
</section>
</li>
<li>
<section class="detail" id="divider">
<h3>divider</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roaddivider" title="enum class in com.here.sdk.mapdata">RoadDivider</a></span> <span class="element-name">divider</span></div>
<div class="block"><p>Indicates the presence of a road divider.</p></div>
</section>
</li>
<li>
<section class="detail" id="isBoatFerry">
<h3>isBoatFerry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBoatFerry</span></div>
<div class="block"><p>Identifies a generalised route of a boat ferry for passengers or vehicles over water.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRailFerry">
<h3>isRailFerry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRailFerry</span></div>
<div class="block"><p>Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied
 on a segment that represent a ferry route for vehicles over rail such as: a route for
 ferrying passengers over rail, if destination is not accessible by the road network or
 prohibits the use of automobiles.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>PhysicalAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PhysicalAttributes</span>()</div>
<div class="block"><p>Creates a new instance with default values.</p></div>
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
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
