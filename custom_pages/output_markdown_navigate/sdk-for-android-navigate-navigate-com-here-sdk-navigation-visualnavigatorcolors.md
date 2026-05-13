---
title: "VisualNavigatorColors (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-navigation-visualnavigatorcolors"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VisualNavigatorColors.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.VisualNavigatorColors</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VisualNavigatorColors</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>This class contains colors used by <a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> to render
 the route and the maneuver arrow visualization.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dayColors()">dayColors</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves HERE day color presets for route and maneuver arrow visualization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getManeuverArrowColor()">getManeuverArrowColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color used to draw maneuver arrows on the route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRouteProgressColors(com.here.sdk.routing.SectionTransportMode)">getRouteProgressColors</a><wbr/>(<a href="sdk-for-android-navigate-..-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets route color for visualization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTrafficOnRouteColors()">getTrafficOnRouteColors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets colors used for visualization of traffic conditions on route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#nightColors()">nightColors</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Retrieves HERE night color presets for route and maneuver arrow visualization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setManeuverArrowColor(com.here.sdk.core.Color)">setManeuverArrowColor</a><wbr/>(<a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the color used to draw maneuver arrows on the route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRouteProgressColors(com.here.sdk.routing.SectionTransportMode,com.here.sdk.navigation.RouteProgressColors)">setRouteProgressColors</a><wbr/>(<a href="sdk-for-android-navigate-..-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode,
 <a href="sdk-for-android-navigate-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a> routeProgressColors)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets route color for visualization.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTrafficOnRouteColors(com.here.sdk.navigation.TrafficOnRouteColors)">setTrafficOnRouteColors</a><wbr/>(<a href="sdk-for-android-navigate-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets colors used for visualization of traffic conditions on route.</div>
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
<section class="detail" id="setRouteProgressColors(com.here.sdk.routing.SectionTransportMode,com.here.sdk.navigation.RouteProgressColors)">
<h3>setRouteProgressColors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteProgressColors</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode,
 @NonNull
 <a href="sdk-for-android-navigate-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a> routeProgressColors)</span></div>
<div class="block"><p>Sets route color for visualization.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sectionTransportMode</code> - <p>The section transport mode.</p></dd>
<dd><code>routeProgressColors</code> - <p>The route progress colors.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteProgressColors(com.here.sdk.routing.SectionTransportMode)">
<h3>getRouteProgressColors</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a></span> <span class="element-name">getRouteProgressColors</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode)</span></div>
<div class="block"><p>Gets route color for visualization.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sectionTransportMode</code> - <p>The section transport mode.</p></dd>
<dt>Returns:</dt>
<dd><p>The route color for visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dayColors()">
<h3>dayColors</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span class="element-name">dayColors</span>()</div>
<div class="block"><p>Retrieves HERE day color presets for route and maneuver arrow visualization.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>HERE day color presets for route and maneuver arrow visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="nightColors()">
<h3>nightColors</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span class="element-name">nightColors</span>()</div>
<div class="block"><p>Retrieves HERE night color presets for route and maneuver arrow visualization.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>HERE night color presets for route and maneuver arrow visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverArrowColor()">
<h3>getManeuverArrowColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getManeuverArrowColor</span>()</div>
<div class="block"><p>Gets the color used to draw maneuver arrows on the route.
 </p><p>The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street.
 The alpha channel is ignored. The color is interpreted as fully opaque.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Maneuver arrow color.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverArrowColor(com.here.sdk.core.Color)">
<h3>setManeuverArrowColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverArrowColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>Sets the color used to draw maneuver arrows on the route. The alpha channel is ignored.
 </p><p>The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street.
 The alpha channel is ignored. The color is interpreted as fully opaque.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Maneuver arrow color.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficOnRouteColors()">
<h3>getTrafficOnRouteColors</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a></span> <span class="element-name">getTrafficOnRouteColors</span>()</div>
<div class="block"><p>Gets colors used for visualization of traffic conditions on route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher.
     For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-android-navigate-routeprogresscolors" title="class in com.here.sdk.navigation"><code>RouteProgressColors</code></a> are used instead.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficOnRouteColors(com.here.sdk.navigation.TrafficOnRouteColors)">
<h3>setTrafficOnRouteColors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficOnRouteColors</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a> value)</span></div>
<div class="block"><p>Sets colors used for visualization of traffic conditions on route.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher.
     For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-android-navigate-routeprogresscolors" title="class in com.here.sdk.navigation"><code>RouteProgressColors</code></a> are used instead.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
