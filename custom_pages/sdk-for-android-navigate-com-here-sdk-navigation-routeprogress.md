---
title: "RouteProgress (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routeprogress"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RouteProgress.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.RouteProgress</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RouteProgress</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Contains all the relevant information on the user's progress along a route.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress" title="class in com.here.sdk.navigation">ManeuverProgress</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#maneuverProgress">maneuverProgress</a></code></div>
<div className="col-last even-row-color">
<div className="block">The progress for next and next-next maneuvers (see <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a>).</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-routematchedlocation" title="class in com.here.sdk.navigation">RouteMatchedLocation</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#routeMatchedLocation">routeMatchedLocation</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Route matched location.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#sectionIndex">sectionIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-sectionprogress" title="class in com.here.sdk.navigation">SectionProgress</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#sectionProgress">sectionProgress</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The progress for each <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> from the current one to the last one.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#spanIndex">spanIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#%3Cinit%3E(java.util.List,java.util.List)">RouteProgress</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-sectionprogress" title="class in com.here.sdk.navigation">SectionProgress</a>&gt; sectionProgress,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress" title="class in com.here.sdk.navigation">ManeuverProgress</a>&gt; maneuverProgress)</code></div>
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
<section className="detail" id="sectionIndex">
<h3>sectionIndex</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">sectionIndex</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0. Use <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#routeMatchedLocation"><code>routeMatchedLocation</code></a> instead.</p></div>
</div>
<div className="block"><p>Index of the <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> in the route.
 Note that this section index does not point to the current <a href="sdk-for-android-navigate-com-here-sdk-navigation-sectionprogress" title="class in com.here.sdk.navigation"><code>SectionProgress</code></a>
 but to the route <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> that you can access via <a href="sdk-for-android-navigate-navigatorinterface#getRoute()"><code>NavigatorInterface.getRoute()</code></a>
 and <a href="sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="spanIndex">
<h3>spanIndex</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">spanIndex</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0. Use <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#routeMatchedLocation"><code>routeMatchedLocation</code></a> instead.</p></div>
</div>
<div className="block"><p>Index of the <a href="sdk-for-android-navigate-com-here-sdk-routing-span" title="class in com.here.sdk.routing"><code>Span</code></a> in the route section.</p></div>
</section>
</li>
<li>
<section className="detail" id="sectionProgress">
<h3>sectionProgress</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-sectionprogress" title="class in com.here.sdk.navigation">SectionProgress</a>&gt;</span> <span className="element-name">sectionProgress</span></div>
<div className="block"><p>The progress for each <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> from the current one to the last one.
 Note that the progress information is accumulated successively, therefore information relative
 to the final destination is in the last item of the list. The list is guaranteed to be non-empty.</p></div>
</section>
</li>
<li>
<section className="detail" id="maneuverProgress">
<h3>maneuverProgress</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress" title="class in com.here.sdk.navigation">ManeuverProgress</a>&gt;</span> <span className="element-name">maneuverProgress</span></div>
<div className="block"><p>The progress for next and next-next maneuvers (see <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a>). Note that the list
 can contain at maximum two items (for next and next-next maneuvers) and one or zero when approaching the
 destination.</p></div>
</section>
</li>
<li>
<section className="detail" id="routeMatchedLocation">
<h3>routeMatchedLocation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routematchedlocation" title="class in com.here.sdk.navigation">RouteMatchedLocation</a></span> <span className="element-name">routeMatchedLocation</span></div>
<div className="block"><p>Route matched location.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.util.List,java.util.List)">
<h3>RouteProgress</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteProgress</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-sectionprogress" title="class in com.here.sdk.navigation">SectionProgress</a>&gt; sectionProgress,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverprogress" title="class in com.here.sdk.navigation">ManeuverProgress</a>&gt; maneuverProgress)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sectionProgress</code> - <p>The progress for each <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> from the current one to the last one.
 Note that the progress information is accumulated successively, therefore information relative
 to the final destination is in the last item of the list. The list is guaranteed to be non-empty.</p></dd>
<dd><code>maneuverProgress</code> - <p>The progress for next and next-next maneuvers (see <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a>). Note that the list
 can contain at maximum two items (for next and next-next maneuvers) and one or zero when approaching the
 destination.</p></dd>
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
