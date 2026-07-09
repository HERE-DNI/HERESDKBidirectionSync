---
title: "RasterDataSourceConfiguration (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.datasource.RasterDataSourceConfiguration → com.here.sdk.mapview.datasource.RasterDataSourceConfiguration

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RasterDataSourceConfiguration</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Called on the main thread after fromJsonFile() method finishes loading the configuration.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" class="type-name-link" title="class in com.here.sdk.mapview.datasource"><code>RasterDataSourceConfiguration.Cache</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Configuration of a local data cache.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" class="type-name-link" title="class in com.here.sdk.mapview.datasource"><code>RasterDataSourceConfiguration.Provider</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Configuration of a data provider.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">`RasterDataSourceConfiguration.Cache`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#cache" class="member-name-link"><code>cache</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Local cache configuration.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#ignoreExpiredData" class="member-name-link"><code>ignoreExpiredData</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag indicating whether expired data should be ignored until refreshed.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#name" class="member-name-link"><code>name</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The unique name of the data source.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">`RasterDataSourceConfiguration.Provider`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#provider" class="member-name-link"><code>provider</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Data provider configuration.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      RasterDataSourceConfiguration ( String name, RasterDataSourceConfiguration.Provider provider, RasterDataSourceConfiguration.Cache cache)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RasterDataSourceConfiguration ( String name, RasterDataSourceConfiguration.Provider provider, RasterDataSourceConfiguration.Cache cache,
       boolean ignoreExpiredData)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-name" class="section detail">

    ### name

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span>

    </div>

    <div class="block">

    The unique name of the data source.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-provider" class="section detail">

    ### provider

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a></span> <span class="element-name">provider</span>

    </div>

    <div class="block">

    Data provider configuration.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-cache" class="section detail">

    ### cache

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a></span> <span class="element-name">cache</span>

    </div>

    <div class="block">

    Local cache configuration.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-ignoreExpiredData" class="section detail">

    ### ignoreExpiredData

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">ignoreExpiredData</span>

    </div>

    <div class="block">

    A flag indicating whether expired data should be ignored until refreshed. Default value is false .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-lang-String-com-here-sdk-mapview-datasource-RasterDataSourceConfiguration-Provider-com-here-sdk-mapview-datasource-RasterDataSourceConfiguration-Cache" class="section detail">

    ### RasterDataSourceConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSourceConfiguration</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a> provider, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a> cache)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `name` -

    The unique name of the data source.

    `provider` -

    Data provider configuration.

    `cache` -

    Local cache configuration.

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String-com-here-sdk-mapview-datasource-RasterDataSourceConfiguration-Provider-com-here-sdk-mapview-datasource-RasterDataSourceConfiguration-Cache-boolean" class="section detail">

    ### RasterDataSourceConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSourceConfiguration</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Provider</a> provider, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration.Cache</a> cache, boolean ignoreExpiredData)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `name` -

    The unique name of the data source.

    `provider` -

    Data provider configuration.

    `cache` -

    Local cache configuration.

    `ignoreExpiredData` -

    A flag indicating whether expired data should be ignored until refreshed. Default value is `false`.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

