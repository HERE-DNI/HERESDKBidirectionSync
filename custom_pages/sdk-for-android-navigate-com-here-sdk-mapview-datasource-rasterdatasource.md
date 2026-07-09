---
title: "RasterDataSource (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RasterDataSource.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.datasource.RasterDataSource</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RasterDataSource</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Data source to load map layers using a raster image format (jpg, png).
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
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource#%3Cinit%3E(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a RasterDataSource instance with the provided data source configuration.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource#%3Cinit%3E(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a RasterDataSource instance with the provided data source configuration and
 registers a listener.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource#%3Cinit%3E(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a RasterDataSource instance with the provided raster tile source.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource#%3Cinit%3E(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener)">RasterDataSource</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a RasterDataSource instance with the provided raster tile source and registers
 a listener.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration)">
<h3>RasterDataSource</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RasterDataSource</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration)</span></div>
<div className="block"><p>Creates a RasterDataSource instance with the provided data source configuration.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The map context to associate the data source with.</p></dd>
<dd><code>configuration</code> - <p>The data source configuration object to use.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration,com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>RasterDataSource</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RasterDataSource</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a> configuration,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div className="block"><p>Creates a RasterDataSource instance with the provided data source configuration and
 registers a listener.</p></div>
<dl className="notes">
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource)">
<h3>RasterDataSource</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RasterDataSource</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource)</span></div>
<div className="block"><p>Creates a RasterDataSource instance with the provided raster tile source.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - <p>The map context to associate the data source with.</p></dd>
<dd><code>name</code> - <p>The unique name of the data source.</p></dd>
<dd><code>tileSource</code> - <p>The raster tile source.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.RasterTileSource,com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>RasterDataSource</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RasterDataSource</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> context,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rastertilesource" title="interface in com.here.sdk.mapview.datasource">RasterTileSource</a> tileSource,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div className="block"><p>Creates a RasterDataSource instance with the provided raster tile source and registers
 a listener.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="changeConfiguration(com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate)">
<h3>changeConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">changeConfiguration</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfigurationUpdate</a> configuration)</span></div>
<div className="block"><p>Applies the configuration update to the data source.
 An example for a configuration update is the update
 to a new bearer token for authentication.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>configuration</code> - <p>The data source configuration update to apply.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>addListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div className="block"><p>Add listener for receiving state notifications. The new listener is
 appended to the set of data source listeners as a strong reference and will receive only
 the notifications occurring after the registration. Caller is responsible for releasing
 the strong reference by calling <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasource#removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)"><code>removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>Listener to be added for receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeListener(com.here.sdk.mapview.datasource.RasterDataSourceListener)">
<h3>removeListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener" title="interface in com.here.sdk.mapview.datasource">RasterDataSourceListener</a> listener)</span></div>
<div className="block"><p>Remove a listener from receiving state notifications.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - <p>Listener to be removed from receiving state notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeListeners()">
<h3>removeListeners</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeListeners</span>()</div>
<div className="block"><p>Remove all listeners from receiving state notifications.</p></div>
</section>
</li>
<li>
<section className="detail" id="destroy()">
<h3>destroy</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">destroy</span>()</div>
<div className="block"><p>Frees all internally used resources. After calling this method, the object
 is not usable anymore.</p></div>
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
