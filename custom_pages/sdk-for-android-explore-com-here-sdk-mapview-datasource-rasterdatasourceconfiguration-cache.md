---
title: "RasterDataSourceConfiguration.Cache (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[RasterDataSourceConfiguration](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">RasterDataSourceConfiguration.Cache</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Configuration of a local data cache.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>long</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache#diskSize"
  class="member-name-link"><code>diskSize</code></a></td>
  <td><div class="block">
  The maximum size to use on disk for the cache, in bytes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache#path"
  class="member-name-link"><code>path</code></a></td>
  <td><div class="block">
  The path to the directory to use for the cache.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>Cache(String path)</code></pre></td>
  <td><div class="block">
  Constructs a Cache object from the provided path and a default cache
  size of 32 MiB.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>Cache(String path,
   long diskSize)</code></pre></td>
  <td><div class="block">
  Constructs a Cache object from the provided path and cache size.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="path" class="section detail">

    ### path

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">path</span>

    </div>

    <div class="block">

    The path to the directory to use for the cache. By default, the map
    gets initialized with a data path which can be fetched from
    SDKOptions.cachePath . The cache will be relative to this path,
    unless an absolute path is provided. The cache can be stored in an
    internal/external storage as long as the app has read/write
    permissions. Empty string means the data path will be used for
    caching. If the provided path, either as absolute path or as
    relative path is invalid, then caching will be disabled. There is no
    contraint regarding the existence of the path. If the path does not
    exist but is valid, it will be created.

    </div>

    </div>

  - <div id="diskSize" class="section detail">

    ### diskSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">diskSize</span>

    </div>

    <div class="block">

    The maximum size to use on disk for the cache, in bytes. Default is
    32 MiB. This cache is independent from the map cache as defined via
    SDKOptions . Its size is only limited by the total device storage
    capacity.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.String)" class="section detail">

    ### Cache

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Cache</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> path)</span>

    </div>

    <div class="block">

    Constructs a Cache object from the provided path and a default cache
    size of 32 MiB.

    </div>

    Parameters:  
    `path` -

    The path to the directory to use for the cache. By default, the map
    gets initialized with a data path which can be fetched from
    `SDKOptions.cachePath`. The cache will be relative to this path,
    unless an absolute path is provided. The cache can be stored in an
    internal/external storage as long as the app has read/write
    permissions. Empty string means the data path will be used for
    caching. If the provided path, either as absolute path or as
    relative path is invalid, then caching will be disabled. There is no
    contraint regarding the existence of the path. If the path does not
    exist but is valid, it will be created.

    </div>

  - <div id="<init>(java.lang.String,long)" class="section detail">

    ### Cache

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Cache</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> path,
    long diskSize)</span>

    </div>

    <div class="block">

    Constructs a Cache object from the provided path and cache size.

    </div>

    Parameters:  
    `path` -

    The path to the directory to use for the cache. By default, the map
    gets initialized with a data path which can be fetched from
    `SDKOptions.cachePath`. The cache will be relative to this path,
    unless an absolute path is provided. The cache can be stored in an
    internal/external storage as long as the app has read/write
    permissions. Empty string means the data path will be used for
    caching. If the provided path, either as absolute path or as
    relative path is invalid, then caching will be disabled. There is no
    contraint regarding the existence of the path. If the path does not
    exist but is valid, it will be created.

    `diskSize` -

    The maximum size to use on disk for the cache, in bytes. Default is
    32 MiB. This cache is independent from the map cache as defined via
    `SDKOptions`. Its size is only limited by the total device storage
    capacity.

    </div>

  </div>

</div>

