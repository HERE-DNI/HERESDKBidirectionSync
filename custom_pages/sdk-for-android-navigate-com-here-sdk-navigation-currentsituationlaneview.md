---
title: "CurrentSituationLaneView (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CurrentSituationLaneView.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.CurrentSituationLaneView</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CurrentSituationLaneView</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that provides current situation lane assistance view
 information for the street at the current position of a single lane.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#access">access</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates which vehicle types can access this lane.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">LaneDirectionCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#directionCategory">directionCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates towards which directions this lane leads.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#directions">directions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates which lane directions are available for this lane.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#directionsOnRoute">directionsOnRoute</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates which lane directions are on the route.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#laneMarkings">laneMarkings</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the lane markings between the lanes.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#type">type</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates this lane's properties.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneview#%3Cinit%3E(com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneDirectionCategory,com.here.sdk.navigation.LaneType)">CurrentSituationLaneView</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">LaneDirectionCategory</a> directionCategory,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type)</code></div>
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
<section className="detail" id="access">
<h3>access</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></span> <span className="element-name">access</span></div>
<div className="block"><p>Indicates which vehicle types can access this lane.</p></div>
</section>
</li>
<li>
<section className="detail" id="directionCategory">
<h3>directionCategory</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">LaneDirectionCategory</a></span> <span className="element-name">directionCategory</span></div>
<div className="block"><p>Indicates towards which directions this lane leads.</p></div>
</section>
</li>
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Indicates this lane's properties.</p></div>
</section>
</li>
<li>
<section className="detail" id="laneMarkings">
<h3>laneMarkings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></span> <span className="element-name">laneMarkings</span></div>
<div className="block"><p>Indicates the lane markings between the lanes.</p></div>
</section>
</li>
<li>
<section className="detail" id="directions">
<h3>directions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</span> <span className="element-name">directions</span></div>
<div className="block"><p>Indicates which lane directions are available for this lane.</p></div>
</section>
</li>
<li>
<section className="detail" id="directionsOnRoute">
<h3>directionsOnRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</span> <span className="element-name">directionsOnRoute</span></div>
<div className="block"><p>Indicates which lane directions are on the route. Following those directions keeps the driver on the route.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneDirectionCategory,com.here.sdk.navigation.LaneType)">
<h3>CurrentSituationLaneView</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CurrentSituationLaneView</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirectioncategory" title="class in com.here.sdk.navigation">LaneDirectionCategory</a> directionCategory,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>access</code> - <p>Indicates which vehicle types can access this lane.</p></dd>
<dd><code>directionCategory</code> - <p>Indicates towards which directions this lane leads.</p></dd>
<dd><code>type</code> - <p>Indicates this lane's properties.</p></dd>
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
