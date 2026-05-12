---
title: "RasterDataSource (API Reference)"
slug: "sdk-for-android-navigate-rasterdatasource"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RasterDataSource.html -->
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
<li>Nested | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.RasterDataSource</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RasterDataSource</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Data source to load map layers using a raster image format (jpg, png).
 The example below illustrates how to create a raster data source and how to link it to
 a newly created map layer.
  <pre><code> RasterDataSource rasterDataSource = new RasterDataSource(mapContext, rasterDataSourceConfig);

    MapLayer layer = new MapLayerBuilder()
       // The name and the type of the data source have to be provided.
       // In our case, the name of the raster data source is in rasterDataSourceConfig.
       .withDataSource(rasterDataSourceConfig.name, MapContentType.RASTER_IMAGE)
       .forMap(map)
       .withName("rasterLayer")
       .build();</code></pre></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a href="sdk-for-android-navigate-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a RasterDataSource instance with the provided data source configuration.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a href="sdk-for-android-navigate-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration,
 <a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a RasterDataSource instance with the provided data source configuration and
 registers a listener.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a RasterDataSource instance with the provided raster tile source.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource,
 <a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a RasterDataSource instance with the provided raster tile source and registers
 a listener.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)">addListener</a><wbr/>(<a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add listener for receiving state notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#changeConfiguration(com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate)">changeConfiguration</a><wbr/>(<a href="sdk-for-android-navigate-rasterdatasourceconfigurationupdate" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfigurationUpdate</a> configuration)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies the configuration update to the data source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frees all internally used resources.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)">removeListener</a><wbr/>(<a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove a listener from receiving state notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeListeners()">removeListeners</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove all listeners from receiving state notifications.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration)">
<h3>RasterDataSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a href="sdk-for-android-navigate-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration)</span></div>
<div class="block"><p>Creates a RasterDataSource instance with the provided data source configuration.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The map context to associate the data source with.</p></dd>
<dd><code>configuration</code> - <p>The data source configuration object to use.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>RasterDataSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a href="sdk-for-android-navigate-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration,
 @NonNull
 <a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div class="block"><p>Creates a RasterDataSource instance with the provided data source configuration and
 registers a listener.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The map context to associate the data source with.</p></dd>
<dd><code>configuration</code> - <p>The data source configuration object to use.</p></dd>
<dd><code>listener</code> - <p>The initial listener to be registered for receiving state notifications.
     Due to the asynchronous nature of the data source initialization, the listeners
     registered later might miss some notifications. This listener is guaranteed to
     receive all notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource)">
<h3>RasterDataSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource)</span></div>
<div class="block"><p>Creates a RasterDataSource instance with the provided raster tile source.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The map context to associate the data source with.</p></dd>
<dd><code>name</code> - <p>The unique name of the data source.</p></dd>
<dd><code>tileSource</code> - <p>The raster tile source.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>RasterDataSource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RasterDataSource</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource,
 @NonNull
 <a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div class="block"><p>Creates a RasterDataSource instance with the provided raster tile source and registers
 a listener.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The map context to associate the data source with.</p></dd>
<dd><code>name</code> - <p>The unique name of the data source.</p></dd>
<dd><code>tileSource</code> - <p>The raster tile source.</p></dd>
<dd><code>listener</code> - <p>The initial listener to be registered for receiving state notifications.
     Due to the asynchronous nature of the data source initialization, the listeners
     registered later might miss some notifications. This listener is guaranteed to
     receive all notifications.</p></dd>
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
<section class="detail" id="changeConfiguration(com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate)">
<h3>changeConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">changeConfiguration</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-rasterdatasourceconfigurationupdate" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfigurationUpdate</a> configuration)</span></div>
<div class="block"><p>Applies the configuration update to the data source.
 An example for a configuration update is the update
 to a new bearer token for authentication.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configuration</code> - <p>The data source configuration update to apply.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>addListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div class="block"><p>Add listener for receiving state notifications. The new listener is
 appended to the set of data source listeners as a strong reference and will receive only
 the notifications occurring after the registration. Caller is responsible for releasing
 the strong reference by calling <a href="#removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)"><code>removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>Listener to be added for receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>removeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div class="block"><p>Remove a listener from receiving state notifications.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>Listener to be removed from receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeListeners()">
<h3>removeListeners</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListeners</span>()</div>
<div class="block"><p>Remove all listeners from receiving state notifications.</p></div>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block"><p>Frees all internally used resources. After calling this method, the object
 is not usable anymore.</p></div>
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
