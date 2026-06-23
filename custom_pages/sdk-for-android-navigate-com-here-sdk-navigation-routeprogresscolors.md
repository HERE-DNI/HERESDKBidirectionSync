---
title: "RouteProgressColors (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RouteProgressColors.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.RouteProgressColors</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RouteProgressColors</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>This struct contains colors for the route progress visualization.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ahead">ahead</a></code></div>
<div class="col-last even-row-color">
<div class="block">Color of the route part that lies ahead of the current location.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#behind">behind</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Color of the route part that lies behind of the current location.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#offRoad">offRoad</a></code></div>
<div class="col-last even-row-color">
<div class="block">Color of the dashed line between the map-matched and the off-road destinations.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#outlineAhead">outlineAhead</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Outline color of the route part that lies ahead of the current location.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#outlineBehind">outlineBehind</a></code></div>
<div class="col-last even-row-color">
<div class="block">Outline color of the route part that lies behind of the current location.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.Color,com.here.sdk.core.Color,com.here.sdk.core.Color,com.here.sdk.core.Color)">RouteProgressColors</a><wbr/>(<a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> ahead,
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> behind,
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> outlineAhead,
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> outlineBehind)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="ahead">
<h3>ahead</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">ahead</span></div>
<div class="block"><p>Color of the route part that lies ahead of the current location.</p></div>
</section>
</li>
<li>
<section class="detail" id="behind">
<h3>behind</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">behind</span></div>
<div class="block"><p>Color of the route part that lies behind of the current location.</p></div>
</section>
</li>
<li>
<section class="detail" id="offRoad">
<h3>offRoad</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">offRoad</span></div>
<div class="block"><p>Color of the dashed line between the map-matched and the off-road destinations.</p></div>
</section>
</li>
<li>
<section class="detail" id="outlineAhead">
<h3>outlineAhead</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">outlineAhead</span></div>
<div class="block"><p>Outline color of the route part that lies ahead of the current location.</p></div>
</section>
</li>
<li>
<section class="detail" id="outlineBehind">
<h3>outlineBehind</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">outlineBehind</span></div>
<div class="block"><p>Outline color of the route part that lies behind of the current location.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.Color,com.here.sdk.core.Color,com.here.sdk.core.Color,com.here.sdk.core.Color)">
<h3>RouteProgressColors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteProgressColors</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> ahead,
 @NonNull
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> behind,
 @NonNull
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> outlineAhead,
 @NonNull
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> outlineBehind)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ahead</code> - <p>Color of the route part that lies ahead of the current location.</p></dd>
<dd><code>behind</code> - <p>Color of the route part that lies behind of the current location.</p></dd>
<dd><code>outlineAhead</code> - <p>Outline color of the route part that lies ahead of the current location.</p></dd>
<dd><code>outlineBehind</code> - <p>Outline color of the route part that lies behind of the current location.</p></dd>
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
