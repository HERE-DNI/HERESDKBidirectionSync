---
title: "RasterDataSourceConfiguration.Cache (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache → com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
[RasterDataSourceConfiguration](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">RasterDataSourceConfiguration.Cache</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Configuration of a local data cache.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

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

  `long`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache#diskSize" class="member-name-link"><code>diskSize</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The maximum size to use on disk for the cache, in bytes.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache#path" class="member-name-link"><code>path</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The path to the directory to use for the cache.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      Cache ( String path)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a Cache object from the provided path and a default cache size of 32 MiB.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Cache ( String path,
       long diskSize)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a Cache object from the provided path and cache size.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-path" class="section detail">

    ### path

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">path</span>

    </div>

    <div class="block">

    The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from SDKOptions.cachePath . The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

    </div>

    </div>

  - <div id="sdk-for-android-explore-diskSize" class="section detail">

    ### diskSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">diskSize</span>

    </div>

    <div class="block">

    The maximum size to use on disk for the cache, in bytes. Default is 32 MiB. This cache is independent from the map cache as defined via SDKOptions . Its size is only limited by the total device storage capacity.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-java-lang-String" class="section detail">

    ### Cache

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Cache</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> path)</span>

    </div>

    <div class="block">

    Constructs a Cache object from the provided path and a default cache size of 32 MiB.

    </div>

    Parameters:  
    `path` -

    The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

    </div>

  - <div id="sdk-for-android-explore-init-java-lang-String-long" class="section detail">

    ### Cache

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Cache</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> path, long diskSize)</span>

    </div>

    <div class="block">

    Constructs a Cache object from the provided path and cache size.

    </div>

    Parameters:  
    `path` -

    The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

    `diskSize` -

    The maximum size to use on disk for the cache, in bytes. Default is 32 MiB. This cache is independent from the map cache as defined via `SDKOptions`. Its size is only limited by the total device storage capacity.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

