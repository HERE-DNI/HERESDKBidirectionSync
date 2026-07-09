---
title: "RasterDataSourceConfiguration (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RasterDataSourceConfiguration.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.datasource.RasterDataSourceConfiguration</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RasterDataSourceConfiguration</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Called on the main thread after <code>fromJsonFile()</code> method finishes loading
 the configuration.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a></code></div>
<div className="col-last even-row-color">
<div className="block">Configuration of a local data cache.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Configuration of a data provider.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#cache">cache</a></code></div>
<div className="col-last even-row-color">
<div className="block">Local cache configuration.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#ignoreExpiredData">ignoreExpiredData</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag indicating whether expired data should be ignored until refreshed.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#name">name</a></code></div>
<div className="col-last even-row-color">
<div className="block">The unique name of the data source.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#provider">provider</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Data provider configuration.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache)">RasterDataSourceConfiguration</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a> provider,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a> cache)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#%3Cinit%3E(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache,boolean)">RasterDataSourceConfiguration</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a> provider,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a> cache,
 boolean ignoreExpiredData)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="name">
<h3>name</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">name</span></div>
<div className="block"><p>The unique name of the data source.</p></div>
</section>
</li>
<li>
<section className="detail" id="provider">
<h3>provider</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a></span> <span className="element-name">provider</span></div>
<div className="block"><p>Data provider configuration.</p></div>
</section>
</li>
<li>
<section className="detail" id="cache">
<h3>cache</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a></span> <span className="element-name">cache</span></div>
<div className="block"><p>Local cache configuration.</p></div>
</section>
</li>
<li>
<section className="detail" id="ignoreExpiredData">
<h3>ignoreExpiredData</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">ignoreExpiredData</span></div>
<div className="block"><p>A flag indicating whether expired data should be ignored until refreshed. Default value is <code>false</code>.</p></div>
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
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache)">
<h3>RasterDataSourceConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RasterDataSourceConfiguration</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a> provider,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a> cache)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>The unique name of the data source.</p></dd>
<dd><code>provider</code> - <p>Data provider configuration.</p></dd>
<dd><code>cache</code> - <p>Local cache configuration.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache,boolean)">
<h3>RasterDataSourceConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RasterDataSourceConfiguration</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a> provider,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a> cache,
 boolean ignoreExpiredData)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>The unique name of the data source.</p></dd>
<dd><code>provider</code> - <p>Data provider configuration.</p></dd>
<dd><code>cache</code> - <p>Local cache configuration.</p></dd>
<dd><code>ignoreExpiredData</code> - <p>A flag indicating whether expired data should be ignored until refreshed. Default value is <code>false</code>.</p></dd>
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
