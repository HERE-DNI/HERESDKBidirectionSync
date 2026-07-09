---
title: "PhysicalAttributes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PhysicalAttributes.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.PhysicalAttributes</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PhysicalAttributes</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Physical attributes of the segment.
 <em><strong>Note</strong></em> a road can have more than one attribute at the same time.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-roaddivider" title="enum class in com.here.sdk.mapdata">RoadDivider</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#divider">divider</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the presence of a road divider.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isBoatFerry">isBoatFerry</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Identifies a generalised route of a boat ferry for passengers or vehicles over water.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isBridge">isBridge</a></code></div>
<div className="col-last even-row-color">
<div className="block">Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isDirtRoad">isDirtRoad</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates whether the navigable segment is paved.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isMultiplyDigitized">isMultiplyDigitized</a></code></div>
<div className="col-last even-row-color">
<div className="block">Identifies separately digitised roads, i.e., roads that are digitised with one line per
 direction of traffic instead of one line per road.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isPrivate">isPrivate</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isRailFerry">isRailFerry</a></code></div>
<div className="col-last even-row-color">
<div className="block">Identifies a generalised route of a ferry for passengers or vehicles via rail.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isRoundabout">isRoundabout</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the presence of a roundabout.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#isTunnel">isTunnel</a></code></div>
<div className="col-last even-row-color">
<div className="block">Identifies an enclosed (on all sides) passageway through or under an obstruction.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes#%3Cinit%3E()">PhysicalAttributes</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance with default values.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="isDirtRoad">
<h3>isDirtRoad</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isDirtRoad</span></div>
<div className="block"><p>Indicates whether the navigable segment is paved.
 Paved is primarily used for map display and routing by assigning
 higher penalties to unpaved roads.
 Paved roads are made of concrete, asphalt, cobblestone or brick.
 Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.</p></div>
</section>
</li>
<li>
<section className="detail" id="isTunnel">
<h3>isTunnel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isTunnel</span></div>
<div className="block"><p>Identifies an enclosed (on all sides) passageway through or under an obstruction.
 This attribute can be used for display or route guidance.</p></div>
</section>
</li>
<li>
<section className="detail" id="isBridge">
<h3>isBridge</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isBridge</span></div>
<div className="block"><p>Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.
 Bridge is published on segments that represent significant
 bridges and/or overpasses; elevated roads are not published as bridge.</p></div>
</section>
</li>
<li>
<section className="detail" id="isPrivate">
<h3>isPrivate</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isPrivate</span></div>
<div className="block"><p>Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.
 Allows for unique cartographic representation of roads that restrict public use.
 May be used to avoid routing through a private road.</p></div>
</section>
</li>
<li>
<section className="detail" id="isRoundabout">
<h3>isRoundabout</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRoundabout</span></div>
<div className="block"><p>Indicates the presence of a roundabout.</p></div>
</section>
</li>
<li>
<section className="detail" id="isMultiplyDigitized">
<h3>isMultiplyDigitized</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isMultiplyDigitized</span></div>
<div className="block"><p>Identifies separately digitised roads, i.e., roads that are digitised with one line per
 direction of traffic instead of one line per road.
 It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus
 lane) are located between the separately digitised opposing roadbeds if driver perception
 remains unchanged.</p></div>
</section>
</li>
<li>
<section className="detail" id="divider">
<h3>divider</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-roaddivider" title="enum class in com.here.sdk.mapdata">RoadDivider</a></span> <span className="element-name">divider</span></div>
<div className="block"><p>Indicates the presence of a road divider.</p></div>
</section>
</li>
<li>
<section className="detail" id="isBoatFerry">
<h3>isBoatFerry</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isBoatFerry</span></div>
<div className="block"><p>Identifies a generalised route of a boat ferry for passengers or vehicles over water.</p></div>
</section>
</li>
<li>
<section className="detail" id="isRailFerry">
<h3>isRailFerry</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRailFerry</span></div>
<div className="block"><p>Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied
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
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>PhysicalAttributes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">PhysicalAttributes</span>()</div>
<div className="block"><p>Creates a new instance with default values.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
