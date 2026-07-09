---
title: "JunctionViewLaneAssistance (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- JunctionViewLaneAssistance.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.JunctionViewLaneAssistance</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">JunctionViewLaneAssistance</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that provides lane assistance information for the next complex junction
 in order to keep following the route. It is recommended to indicate <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> separately or to indicate only <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> information -
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a> will recommend all lanes that allow to pass the upcoming complex junction, regardless
 if they will lead to the next maneuver or not.
 If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be
 the same as the ones from <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a>.
 A junction is recognized as complex only if:
 <ul>
<li>it is at least a bifurcation;</li>
<li>it has at least two lanes whose directions do not follow the current route.
 In opposition to <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a>, notifications are also forwarded when there is
 no maneuver action occurring at the next complex junction.
 Therefore, <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a> can be disjointed from maneuvers. If lane assistance should be used to
 associate it with upcoming maneuvers, consider to use <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> instead.
 Note that <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistance" title="class in com.here.sdk.navigation"><code>ManeuverViewLaneAssistance</code></a> notifications are synchronized with maneuver events,
 whereas <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation"><code>JunctionViewLaneAssistance</code></a> events are not strictly synchronized with maneuver events.</li>
</ul></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#distanceToJunctionInMeters">distanceToJunctionInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance to the next complex junction in meters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#lanesForNextJunction">lanesForNextJunction</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A list of lanes on the next complex junction.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance#%3Cinit%3E(java.util.List,double)">JunctionViewLaneAssistance</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextJunction,
 double distanceToJunctionInMeters)</code></div>
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
<section className="detail" id="lanesForNextJunction">
<h3>lanesForNextJunction</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt;</span> <span className="element-name">lanesForNextJunction</span></div>
<div className="block"><p>A list of lanes on the next complex junction.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
 countries. An empty list means that the complex junction has been passed and that the lane information is not
 valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
 one event with an empty list afterwards.
 <strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceToJunctionInMeters">
<h3>distanceToJunctionInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceToJunctionInMeters</span></div>
<div className="block"><p>Distance to the next complex junction in meters.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.util.List,double)">
<h3>JunctionViewLaneAssistance</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">JunctionViewLaneAssistance</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lane" title="class in com.here.sdk.navigation">Lane</a>&gt; lanesForNextJunction,
 double distanceToJunctionInMeters)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lanesForNextJunction</code> - <p>A list of lanes on the next complex junction.
 The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
 the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
 countries. An empty list means that the complex junction has been passed and that the lane information is not
 valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
 one event with an empty list afterwards.
 <strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p></dd>
<dd><code>distanceToJunctionInMeters</code> - <p>Distance to the next complex junction in meters.</p></dd>
</dl>
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
