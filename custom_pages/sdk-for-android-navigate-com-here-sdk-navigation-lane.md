---
title: "Lane (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lane"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Lane.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.Lane</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Lane</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that provides information for a lane.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#access">access</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates which vehicle types can access this lane.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directions">directions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates all the lane directions that are available for this lane.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directionsOnRoute">directionsOnRoute</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the lane directions that are on the route.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#laneMarkings">laneMarkings</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the lane markings between the lanes.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#recommendationState">recommendationState</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates if this lane leads to the upcoming maneuvers.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#type">type</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates the properties of this lane.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#%3Cinit%3E(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">Lane</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#%3Cinit%3E(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneRecommendationState,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">Lane</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a> recommendationState,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</code></div>
<div className="col-last odd-row-color">
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
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Indicates the properties of this lane.
 For example, it indicates whether parking is allowed, if it is an acceleration lane,
 an express lane, or other attributes.</p></div>
</section>
</li>
<li>
<section className="detail" id="recommendationState">
<h3>recommendationState</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a></span> <span className="element-name">recommendationState</span></div>
<div className="block"><p>Indicates if this lane leads to the upcoming maneuvers.</p></div>
</section>
</li>
<li>
<section className="detail" id="access">
<h3>access</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></span> <span className="element-name">access</span></div>
<div className="block"><p>Indicates which vehicle types can access this lane.</p></div>
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
<div className="block"><p>Indicates all the lane directions that are available for this lane.</p></div>
</section>
</li>
<li>
<section className="detail" id="directionsOnRoute">
<h3>directionsOnRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</span> <span className="element-name">directionsOnRoute</span></div>
<div className="block"><p>Indicates the lane directions that are on the route.
 Following these directions keeps the driver on the route.
 This is a subset of <a href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directions"><code>directions</code></a>.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneRecommendationState,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">
<h3>Lane</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Lane</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a> recommendationState,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>Indicates the properties of this lane.
 For example, it indicates whether parking is allowed, if it is an acceleration lane,
 an express lane, or other attributes.</p></dd>
<dd><code>recommendationState</code> - <p>Indicates if this lane leads to the upcoming maneuvers.</p></dd>
<dd><code>access</code> - <p>Indicates which vehicle types can access this lane.</p></dd>
<dd><code>laneMarkings</code> - <p>Indicates the lane markings between the lanes.</p></dd>
<dd><code>directions</code> - <p>Indicates all the lane directions that are available for this lane.</p></dd>
<dd><code>directionsOnRoute</code> - <p>Indicates the lane directions that are on the route.
 Following these directions keeps the driver on the route.
 This is a subset of <a href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directions"><code>directions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">
<h3>Lane</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Lane</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>Indicates the properties of this lane.
 For example, it indicates whether parking is allowed, if it is an acceleration lane,
 an express lane, or other attributes.</p></dd>
<dd><code>access</code> - <p>Indicates which vehicle types can access this lane.</p></dd>
<dd><code>laneMarkings</code> - <p>Indicates the lane markings between the lanes.</p></dd>
<dd><code>directions</code> - <p>Indicates all the lane directions that are available for this lane.</p></dd>
<dd><code>directionsOnRoute</code> - <p>Indicates the lane directions that are on the route.
 Following these directions keeps the driver on the route.
 This is a subset of <a href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directions"><code>directions</code></a>.</p></dd>
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
