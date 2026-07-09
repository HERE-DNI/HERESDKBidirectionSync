---
title: "VisualNavigatorColors (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VisualNavigatorColors.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.VisualNavigatorColors</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VisualNavigatorColors</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This class contains colors used by <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation"><code>VisualNavigator</code></a> to render
 the route and the maneuver arrow visualization.</p></div>
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
<section className="detail" id="setRouteProgressColors(com.here.sdk.routing.SectionTransportMode,com.here.sdk.navigation.RouteProgressColors)">
<h3>setRouteProgressColors</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRouteProgressColors</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a> routeProgressColors)</span></div>
<div className="block"><p>Sets route color for visualization.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sectionTransportMode</code> - <p>The section transport mode.</p></dd>
<dd><code>routeProgressColors</code> - <p>The route progress colors.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRouteProgressColors(com.here.sdk.routing.SectionTransportMode)">
<h3>getRouteProgressColors</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a></span> <span className="element-name">getRouteProgressColors</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode)</span></div>
<div className="block"><p>Gets route color for visualization.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sectionTransportMode</code> - <p>The section transport mode.</p></dd>
<dt>Returns:</dt>
<dd><p>The route color for visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="dayColors()">
<h3>dayColors</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span className="element-name">dayColors</span>()</div>
<div className="block"><p>Retrieves HERE day color presets for route and maneuver arrow visualization.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>HERE day color presets for route and maneuver arrow visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="nightColors()">
<h3>nightColors</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span className="element-name">nightColors</span>()</div>
<div className="block"><p>Retrieves HERE night color presets for route and maneuver arrow visualization.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>HERE night color presets for route and maneuver arrow visualization.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getManeuverArrowColor()">
<h3>getManeuverArrowColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getManeuverArrowColor</span>()</div>
<div className="block"><p>Gets the color used to draw maneuver arrows on the route.
 The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street.
 The alpha channel is ignored. The color is interpreted as fully opaque.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Maneuver arrow color.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setManeuverArrowColor(com.here.sdk.core.Color)">
<h3>setManeuverArrowColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setManeuverArrowColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Sets the color used to draw maneuver arrows on the route. The alpha channel is ignored.
 The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street.
 The alpha channel is ignored. The color is interpreted as fully opaque.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Maneuver arrow color.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficOnRouteColors()">
<h3>getTrafficOnRouteColors</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a></span> <span className="element-name">getTrafficOnRouteColors</span>()</div>
<div className="block"><p>Gets colors used for visualization of traffic conditions on route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher.
     For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation"><code>RouteProgressColors</code></a> are used instead.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrafficOnRouteColors(com.here.sdk.navigation.TrafficOnRouteColors)">
<h3>setTrafficOnRouteColors</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrafficOnRouteColors</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a> value)</span></div>
<div className="block"><p>Sets colors used for visualization of traffic conditions on route.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher.
     For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation"><code>RouteProgressColors</code></a> are used instead.</p></dd>
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
