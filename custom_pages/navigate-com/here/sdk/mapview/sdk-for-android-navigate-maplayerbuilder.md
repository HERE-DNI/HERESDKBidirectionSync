---
title: "MapLayerBuilder (API Reference)"
slug: "sdk-for-android-navigate-maplayerbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapLayerBuilder.html -->
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
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapLayerBuilder</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapLayerBuilder</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>MapLayerBuilder is used to add layers to a map to visualise a dataset in a
 programmatic way without defining it upfront in the configuration files.
 <p>For example, after loading a scene configuration file, the renderer is setup to draw layers in the
 following order:
 <ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>Rendering order of elements in
 a single map layer can be controlled with categories. Layer names are unique, and category names have
 to be unique within a layer. The layer's default, main category is unnamed.
 <p>The concept of 'category' is tightly linked to styling. The idea behind category is that
 one should be able to style separately elements in a map layer. Take, for instance, roads.
 If one wants to style separately the bridges it will create a category 'bridges' and style
 it accordingly in the style file. If the user does not intend to or cannot style elements of
 the layer differently then it should opt for a layer with only the default category (e.g.
 for a raster layer, only the default category makes sense, since the layer has no other
 stylable elements apart from the raster image).
 <p>A new layer called 'zone' and its category 'background' can be added dynamically so that the
 rendering order gets modified in the following way:
 <ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the
 following example:
   <pre><code> MapLayerPriority layerPriority = new MapLayerPriorityBuilder()
        .renderedAfterLayer("water") // places main category after 'water'
        .withCategory("background")
        .renderedAfterLayer("water") // places 'background' category after 'water' and before the
                                     // layer's main category.
        .build();

     MapLayer layer = new MapLayerBuilder()
        .withDataSource("DataSourceName", MapContentType.LINE)
        .forMap(map)
        .withName("zone")
        .withPriority(layerPriority)
        .build();</code></pre>
<p>In case no layer priority or an empty one is provided, or if a reference layer-category pair is not
 present in the rendering order, the layer is going to be rendered last with respect to the rendering
 order at the time of its creation.
 <p>Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers.
 All labels will be rendered within the "labels" layer, defined in the scene configuration file.
 By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed.
 The following categories can be used to have a different behaviour:
 <ul>
<li>'custom-labels' A label should be rendered first, is allowed to overlap with other labels of
 the same category and block map labels.</li>
<li>'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed
 to overlap with other labels of the same categoty and block map labels.</li>
<li>'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all
 predefined categories, also map labels.
 These categories are configured accordingly in the basic map
 scene configurations.
 Category assignment to features can be done in the style based on data attributes. The category
 assignment can be done for all types of content: point, line, polygon.</li>
</ul></p></p></p></p></p></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-maplayerbuilder.instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapLayerBuilder.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to build a <a href="sdk-for-android-navigate-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-maplayerbuilder.instantiationerrordetails" title="class in com.here.sdk.mapview">MapLayerBuilder.InstantiationErrorDetails</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Describes the reason for failing to build a <a href="sdk-for-android-navigate-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-maplayerbuilder.instantiationexception" title="class in com.here.sdk.mapview">MapLayerBuilder.InstantiationException</a></code></div>
<div class="col-last even-row-color">
<div class="block">Thrown when failing to build a <a href="sdk-for-android-navigate-maplayer" title="class in com.here.sdk.mapview"><code>MapLayer</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MapLayerBuilder</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of the layer builder interface.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayer" title="class in com.here.sdk.mapview">MapLayer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#build()">build</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Constructs, registers and configures a new map layer showing specified content type
 according to the configured parameters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#forMap(com.here.sdk.mapview.HereMap)">forMap</a><wbr/>(<a href="sdk-for-android-navigate-heremap" title="class in com.here.sdk.mapview">HereMap</a> targetMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to display a layer in the given map.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withDataSource(java.lang.String,com.here.sdk.mapview.MapContentType)">withDataSource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dataSourceName,
 <a href="sdk-for-android-navigate-mapcontenttype" title="enum class in com.here.sdk.mapview">MapContentType</a> contentType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to use a data source with the given name as the source
 of data for the layer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withLoadPriority(double)">withLoadPriority</a><wbr/>(double loadPriority)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to set the layer load priority.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withMapMeasureDependentStorageLevels(com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels)">withMapMeasureDependentStorageLevels</a><wbr/>(<a href="sdk-for-android-navigate-maplayermapmeasuredependentstoragelevels" title="class in com.here.sdk.mapview">MapLayerMapMeasureDependentStorageLevels</a> mapLayerMapMeasureDependentStorageLevels)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies a mapping from the map measure to the storage level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withName(java.lang.String)">withName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures builder to use the given name as a layer name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withPriority(com.here.sdk.mapview.MapLayerPriority)">withPriority</a><wbr/>(<a href="sdk-for-android-navigate-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to set the MapLayerPriority to be used by the layer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withStyle(com.here.sdk.mapview.Style)">withStyle</a><wbr/>(<a href="sdk-for-android-navigate-style" title="class in com.here.sdk.mapview">Style</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to use a style.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#withVisibilityRange(com.here.sdk.mapview.MapLayerVisibilityRange)">withVisibilityRange</a><wbr/>(<a href="sdk-for-android-navigate-maplayervisibilityrange" title="class in com.here.sdk.mapview">MapLayerVisibilityRange</a> visibilityRange)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Configures the builder to set the layer visible in the given zoom levels range.</div>
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

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>MapLayerBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapLayerBuilder</span>()</div>
<div class="block"><p>Creates an instance of the layer builder interface.</p></div>
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
<section class="detail" id="withName(java.lang.String)">
<h3>withName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withName</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block"><p>Configures builder to use the given name as a layer name.
 The name is a mandatory layer creation parameter.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>Name of the layer. Must be unique.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withDataSource(java.lang.String,com.here.sdk.mapview.MapContentType)">
<h3>withDataSource</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withDataSource</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dataSourceName,
 @NonNull
 <a href="sdk-for-android-navigate-mapcontenttype" title="enum class in com.here.sdk.mapview">MapContentType</a> contentType)</span></div>
<div class="block"><p>Configures the builder to use a data source with the given name as the source
 of data for the layer.
 The datasource name and content type are mandatory layer creation parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataSourceName</code> - <p>Name of the data source.</p></dd>
<dd><code>contentType</code> - <p>The renderable content type supplied by the data source.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withStyle(com.here.sdk.mapview.Style)">
<h3>withStyle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withStyle</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-style" title="class in com.here.sdk.mapview">Style</a> style)</span></div>
<div class="block"><p>Configures the builder to use a style.
 Providing a style during layer creation is not mandatory. The style can also be set/updated after the layer creation.
 For more details see Custom Layer Style Reference in the documentation.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - <p>Style for the layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="forMap(com.here.sdk.mapview.HereMap)">
<h3>forMap</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">forMap</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-heremap" title="class in com.here.sdk.mapview">HereMap</a> targetMap)</span></div>
<div class="block"><p>Configures the builder to display a layer in the given map.
 The map is a mandatory layer creation parameter.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targetMap</code> - <p>The map.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withPriority(com.here.sdk.mapview.MapLayerPriority)">
<h3>withPriority</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withPriority</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a> priority)</span></div>
<div class="block"><p>Configures the builder to set the MapLayerPriority to be used by the layer.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>priority</code> - <p>MapLayerPriority which should be applied to the layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withVisibilityRange(com.here.sdk.mapview.MapLayerVisibilityRange)">
<h3>withVisibilityRange</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withVisibilityRange</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maplayervisibilityrange" title="class in com.here.sdk.mapview">MapLayerVisibilityRange</a> visibilityRange)</span></div>
<div class="block"><p>Configures the builder to set the layer visible in the given zoom levels range.
 Values outside the map zoom level range (0, 24) will be ignored.
 Providing the visibility range is optional. If not provided, the layer will be visible
 on all zoom levels.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visibilityRange</code> - <p>Visibility range which should be applied to the layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withMapMeasureDependentStorageLevels(com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels)">
<h3>withMapMeasureDependentStorageLevels</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withMapMeasureDependentStorageLevels</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maplayermapmeasuredependentstoragelevels" title="class in com.here.sdk.mapview">MapLayerMapMeasureDependentStorageLevels</a> mapLayerMapMeasureDependentStorageLevels)</span></div>
<div class="block"><p>Applies a mapping from the map measure to the storage level. This mapping is used by the layer to request data
 for the specified storage level corresponding to the map measure from the datasource.
 This can be used for example to fine-tune the resolution of raster layers.
 Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon.
 Note: Mappings that request higher storage levels will lead to an increased number
 of requests to the raster tile service.
 Providing the map measure to storage level mapping is optional. If not provided, the default mapping will
 use a storage level that is for raster layers one and for others three levels lower than the zoom level,
 corresponding to an offset of -1 and -3.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapLayerMapMeasureDependentStorageLevels</code> - <p>The map measure to storage level mapping that should be applied for the layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withLoadPriority(double)">
<h3>withLoadPriority</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayerbuilder" title="class in com.here.sdk.mapview">MapLayerBuilder</a></span> <span class="element-name">withLoadPriority</span><wbr/><span class="parameters">(double loadPriority)</span></div>
<div class="block"><p>Configures the builder to set the layer load priority.
 Higher load priority values lead to layer being scheduled for loading before layers with lesser values.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>loadPriority</code> - <p>Load priority for layer.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="build()">
<h3>build</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maplayer" title="class in com.here.sdk.mapview">MapLayer</a></span> <span class="element-name">build</span>()
               throws <span class="exceptions"><a href="sdk-for-android-navigate-maplayerbuilder.instantiationexception" title="class in com.here.sdk.mapview">MapLayerBuilder.InstantiationException</a></span></div>
<div class="block"><p>Constructs, registers and configures a new map layer showing specified content type
 according to the configured parameters.
 After this call this instance is reset to the initial state. It could be used to build another
 map layer, but will not keep any previously configured properties.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A new MapLayer instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-maplayerbuilder.instantiationexception" title="class in com.here.sdk.mapview">MapLayerBuilder.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
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
