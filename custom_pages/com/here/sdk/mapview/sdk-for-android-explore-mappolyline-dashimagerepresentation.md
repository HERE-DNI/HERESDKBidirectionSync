---
title: "Untitled"
slug: "sdk-for-android-explore-mappolyline-dashimagerepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolyline.DashImageRepresentation.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>
<h1 class="title" title="Class MapPolyline.DashImageRepresentation">Class MapPolyline.DashImageRepresentation</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="sdk-for-android-explore-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div class="inheritance"><a href="sdk-for-android-explore-mappolyline-representation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapPolyline.Representation</a>
<div class="inheritance">com.here.sdk.mapview.MapPolyline.DashImageRepresentation</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapPolyline.DashImageRepresentation</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div class="block"><p>Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
 from each other.
 <p>This dash pattern representation consists only of images rendered at certain
 points along the polyline. For rendering them without any distortions, polyline gets sliced into
 series of straight segments that are multiple of sum of dash and gap lengths. For this
 reason, the new polyline geometry might not align fully with original geometry.
 <p>The <a href="#getDashImage()"><code>getDashImage()</code></a> is stretched according to <a href="#getDashLength()"><code>getDashLength()</code></a>
 and <a href="#getDashWidth()"><code>getDashWidth()</code></a>, with image's width matched to <code>dashLength</code> and
 image's height matched to <code>dashWidth</code>. The image is oriented so that its bottom is on the
 left-hand side between vertices <code>n</code> and <code>n+1</code>.
 <p>The spacing between images is specified by <a href="#getGapLength()"><code>getGapLength()</code></a>.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></p></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.here.sdk.mapview.MapPolyline.Representation">Nested classes/interfaces inherited from class com.here.sdk.mapview.<a href="sdk-for-android-explore-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></h2>
<code><a href="sdk-for-android-explore-mappolyline-representation-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a>, <a href="sdk-for-android-explore-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">DashImageRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a uniform dash pattern in which the length of a gap is the same as the length of
 a dash.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">DashImageRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a simple dash pattern in which the lengths of a dash and gap can be different.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDashImage()">getDashImage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the image that is rendered in place of dash space.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDashLength()">getDashLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent length of a dash, to which image width is stretched.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDashWidth()">getDashWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent width of a dash, to which image height is stretched.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGapLength()">getGapLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent length of a gap between dash images.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">
<h3>DashImageRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DashImageRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 @NonNull
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span>
                        throws <span class="exceptions"><a href="sdk-for-android-explore-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a uniform dash pattern in which the length of a gap is the same as the length of
 a dash. Dashes are rendered as image.
 <p>This allows for patterns like <code>' — — — —'</code> or <code>' —— —— ——'</code>.
 <p>For <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> supplied for <code>dashLength</code> and <code>dashWidth</code>,
 only <a href="sdk-for-android-explore-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported for <a href="sdk-for-android-explore-mapmeasuredependentrendersize#measureKind"><code>MapMeasureDependentRenderSize.measureKind</code></a>
 and only <a href="sdk-for-android-explore-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> is supported for <a href="sdk-for-android-explore-mapmeasuredependentrendersize#sizeUnit"><code>MapMeasureDependentRenderSize.sizeUnit</code></a>.
 <p>Only map measure values in range [3-19] are supported.
 <p>The value of the keys in <a href="sdk-for-android-explore-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> is truncated to integer values,
 hence only a single value can be provided per zoom level.
 <p>The values are interpolated linearly between zoom levels.</p></p></p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dashLength</code> - <p>The map measure dependent length of a dash, to which image width is stretched.</p></dd>
<dd><code>dashWidth</code> - <p>The map measure dependent width of a dash, to which image height is stretched.</p></dd>
<dd><code>image</code> - <p>Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">
<h3>DashImageRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DashImageRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 @NonNull
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span>
                        throws <span class="exceptions"><a href="sdk-for-android-explore-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.
 Dashes are rendered as image.
 <p>This allows for patterns like <code>' — — — —'</code> or <code>' ——— ——— ———'</code>.
 <p>For <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> supplied for <code>dashLength</code>, <code>gapLength</code> and <code>dashWidth</code>,
 only <a href="sdk-for-android-explore-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported for <a href="sdk-for-android-explore-mapmeasuredependentrendersize#measureKind"><code>MapMeasureDependentRenderSize.measureKind</code></a>
 and only <a href="sdk-for-android-explore-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> is supported for <a href="sdk-for-android-explore-mapmeasuredependentrendersize#sizeUnit"><code>MapMeasureDependentRenderSize.sizeUnit</code></a>.
 <p>Only map measure values in range [3-19] are supported.
 <p>The value of the keys in <a href="sdk-for-android-explore-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> is truncated to integer values,
 hence only a single value can be provided per zoom level.
 <p>The values are interpolated linearly between zoom levels.</p></p></p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dashLength</code> - <p>The map measure dependent length of a dash, to which image width is stretched.</p></dd>
<dd><code>gapLength</code> - <p>The map measure dependent length of a gap between dash images.</p></dd>
<dd><code>dashWidth</code> - <p>The map measure dependent width of a dash, to which image height is stretched.</p></dd>
<dd><code>image</code> - <p>Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getDashImage()">
<h3>getDashImage</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span class="element-name">getDashImage</span>()</div>
<div class="block"><p>Gets the image that is rendered in place of dash space.
 <p>It is stretched to fill whole polyline width and length of each dash.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Image to be rendered in place of dash space.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDashLength()">
<h3>getDashLength</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getDashLength</span>()</div>
<div class="block"><p>Gets the map measure dependent length of a dash, to which image width is stretched.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map measure dependent length of a dash, to which image width is stretched.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGapLength()">
<h3>getGapLength</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getGapLength</span>()</div>
<div class="block"><p>Gets the map measure dependent length of a gap between dash images.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map measure dependent length of a gap between dash images.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDashWidth()">
<h3>getDashWidth</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getDashWidth</span>()</div>
<div class="block"><p>Gets the map measure dependent width of a dash, to which image height is stretched.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map measure dependent width of a dash, to which image height is stretched.</p></dd>
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
</body>
</html>

</div>
`
}</HTMLBlock>
