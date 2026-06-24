---
title: "Lane (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lane"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Lane.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.Lane</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Lane</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class that provides information for a lane.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#access">access</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates which vehicle types can access this lane.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directions">directions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates all the lane directions that are available for this lane.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directionsOnRoute">directionsOnRoute</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the lane directions that are on the route.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#laneMarkings">laneMarkings</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the lane markings between the lanes.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#recommendationState">recommendationState</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates if this lane leads to the upcoming maneuvers.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-lanetype" title="class in com.here.sdk.navigation">LaneType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#type">type</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the properties of this lane.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#%3Cinit%3E(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">Lane</a><wbr/>(<a href="sdk-for-android-navigate-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 <a href="sdk-for-android-navigate-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 <a href="sdk-for-android-navigate-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#%3Cinit%3E(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneRecommendationState,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">Lane</a><wbr/>(<a href="sdk-for-android-navigate-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 <a href="sdk-for-android-navigate-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a> recommendationState,
 <a href="sdk-for-android-navigate-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 <a href="sdk-for-android-navigate-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lane#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lanetype" title="class in com.here.sdk.navigation">LaneType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>Indicates the properties of this lane.
 For example, it indicates whether parking is allowed, if it is an acceleration lane,
 an express lane, or other attributes.</p></div>
</section>
</li>
<li>
<section class="detail" id="recommendationState">
<h3>recommendationState</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a></span> <span class="element-name">recommendationState</span></div>
<div class="block"><p>Indicates if this lane leads to the upcoming maneuvers.</p></div>
</section>
</li>
<li>
<section class="detail" id="access">
<h3>access</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></span> <span class="element-name">access</span></div>
<div class="block"><p>Indicates which vehicle types can access this lane.</p></div>
</section>
</li>
<li>
<section class="detail" id="laneMarkings">
<h3>laneMarkings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></span> <span class="element-name">laneMarkings</span></div>
<div class="block"><p>Indicates the lane markings between the lanes.</p></div>
</section>
</li>
<li>
<section class="detail" id="directions">
<h3>directions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</span> <span class="element-name">directions</span></div>
<div class="block"><p>Indicates all the lane directions that are available for this lane.</p></div>
</section>
</li>
<li>
<section class="detail" id="directionsOnRoute">
<h3>directionsOnRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt;</span> <span class="element-name">directionsOnRoute</span></div>
<div class="block"><p>Indicates the lane directions that are on the route.
 Following these directions keeps the driver on the route.
 This is a subset of <a href="sdk-for-android-navigate-com-here-sdk-navigation-lane#directions"><code>directions</code></a>.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneRecommendationState,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">
<h3>Lane</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Lane</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-lanerecommendationstate" title="enum class in com.here.sdk.navigation">LaneRecommendationState</a> recommendationState,
 @NonNull
 <a href="sdk-for-android-navigate-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 @NonNull
 <a href="sdk-for-android-navigate-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.LaneType,com.here.sdk.navigation.LaneAccess,com.here.sdk.navigation.LaneMarkings,java.util.List,java.util.List)">
<h3>Lane</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Lane</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-lanetype" title="class in com.here.sdk.navigation">LaneType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 @NonNull
 <a href="sdk-for-android-navigate-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> laneMarkings,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directions,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-lanedirection" title="enum class in com.here.sdk.navigation">LaneDirection</a>&gt; directionsOnRoute)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
