---
title: "RoadAttributes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadattributes"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoadAttributes.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.RoadAttributes</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RoadAttributes</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Road attributes, including usage and physical characteristics.
 Note that a road can have more than one attribute at the same time.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isBridge">isBridge</a></code></div>
<div className="col-last even-row-color">
<div className="block">Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isBuiltUpArea">isBuiltUpArea</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates if the navigable segment is a built up area.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isControlledAccess">isControlledAccess</a></code></div>
<div className="col-last even-row-color">
<div className="block">Controlled access roads are roads with limited entrances and exits
 that allow uninterrupted high-speed traffic flow.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isDirtRoad">isDirtRoad</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates whether the navigable segment is paved.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isDividedRoad">isDividedRoad</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates if there is a physical structure or painted road marking intended to legally
 prohibit left turns in right-side driving countries, right turns in left-side driving
 countries, and U-turns at divided intersections or in the middle of divided segments.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isNoThrough">isNoThrough</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Identifies a no through road.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isPrivate">isPrivate</a></code></div>
<div className="col-last even-row-color">
<div className="block">Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRamp">isRamp</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Range is a ramp: connects roads that do not intersect at grade.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRightDrivingSide">isRightDrivingSide</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isRoundabout">isRoundabout</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the presence of a roundabout.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isTollway">isTollway</a></code></div>
<div className="col-last even-row-color">
<div className="block">Identifies a road for which a fee must be paid to use the road.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#isTunnel">isTunnel</a></code></div>
<div className="col-last odd-row-color">
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes#%3Cinit%3E()">RoadAttributes</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<section className="detail" id="isRamp">
<h3>isRamp</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRamp</span></div>
<div className="block"><p>Range is a ramp: connects roads that do not intersect at grade.
 Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”)
 and for route guidance when determining if sign text should be used.</p></div>
</section>
</li>
<li>
<section className="detail" id="isControlledAccess">
<h3>isControlledAccess</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isControlledAccess</span></div>
<div className="block"><p>Controlled access roads are roads with limited entrances and exits
 that allow uninterrupted high-speed traffic flow.
 For example, the Interstate/Freeway network in the United States or
 the Motorway network in Europe.
 Controlled Access can be used for map display, avoidance of freeway/motorway,
 publishing speed limits, and route guidance timing.</p></div>
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
<section className="detail" id="isNoThrough">
<h3>isNoThrough</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isNoThrough</span></div>
<div className="block"><p>Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.</p></div>
</section>
</li>
<li>
<section className="detail" id="isTollway">
<h3>isTollway</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isTollway</span></div>
<div className="block"><p>Identifies a road for which a fee must be paid to use the road.
 Tollway may be used for map display (e.g., different rendering of toll roads) and routing.
 Tollway is flagged on roads that require a fee for traversal.</p></div>
</section>
</li>
<li>
<section className="detail" id="isDividedRoad">
<h3>isDividedRoad</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isDividedRoad</span></div>
<div className="block"><p>Indicates if there is a physical structure or painted road marking intended to legally
 prohibit left turns in right-side driving countries, right turns in left-side driving
 countries, and U-turns at divided intersections or in the middle of divided segments.</p></div>
</section>
</li>
<li>
<section className="detail" id="isRightDrivingSide">
<h3>isRightDrivingSide</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRightDrivingSide</span></div>
<div className="block"><p>Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.
 For example, in New York it is always <code>true</code> and in London always <code>false</code> as the United Kingdom is
 a left-hand driving country.</p></div>
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
<section className="detail" id="isBuiltUpArea">
<h3>isBuiltUpArea</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isBuiltUpArea</span></div>
<div className="block"><p>Indicates if the navigable segment is a built up area.</p></div>
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
<h3>RoadAttributes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RoadAttributes</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
