---
title: "RasterDataSourceConfiguration (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.datasource.RasterDataSourceConfiguration

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RasterDataSourceConfiguration</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Called on the main thread after fromJsonFile() method finishes loading
the configuration.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

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
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache"
  class="type-name-link"
  title="class in com.here.sdk.mapview.datasource"><code>RasterDataSourceConfiguration.Cache</code></a></td>
  <td><div class="block">
  Configuration of a local data cache.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
  class="type-name-link"
  title="class in com.here.sdk.mapview.datasource"><code>RasterDataSourceConfiguration.Provider</code></a></td>
  <td><div class="block">
  Configuration of a data provider.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache"
  title="class in com.here.sdk.mapview.datasource"><code>RasterDataSourceConfiguration.Cache</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#cache"
  class="member-name-link"><code>cache</code></a></td>
  <td><div class="block">
  Local cache configuration.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#ignoreExpiredData"
  class="member-name-link"><code>ignoreExpiredData</code></a></td>
  <td><div class="block">
  A flag indicating whether expired data should be ignored until
  refreshed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#name"
  class="member-name-link"><code>name</code></a></td>
  <td><div class="block">
  The unique name of the data source.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider"
  title="class in com.here.sdk.mapview.datasource"><code>RasterDataSourceConfiguration.Provider</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration#provider"
  class="member-name-link"><code>provider</code></a></td>
  <td><div class="block">
  Data provider configuration.
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
  <td><pre><code>RasterDataSourceConfiguration(String name,
   RasterDataSourceConfiguration.Provider provider,
   RasterDataSourceConfiguration.Cache cache)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>RasterDataSourceConfiguration(String name,
   RasterDataSourceConfiguration.Provider provider,
   RasterDataSourceConfiguration.Cache cache,
   boolean ignoreExpiredData)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
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

  - <div id="name" class="section detail">

    ### name

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span>

    </div>

    <div class="block">

    The unique name of the data source.

    </div>

    </div>

  - <div id="provider" class="section detail">

    ### provider

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RasterDataSourceConfiguration.Provider](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">provider</span>

    </div>

    <div class="block">

    Data provider configuration.

    </div>

    </div>

  - <div id="cache" class="section detail">

    ### cache

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[RasterDataSourceConfiguration.Cache](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">cache</span>

    </div>

    <div class="block">

    Local cache configuration.

    </div>

    </div>

  - <div id="ignoreExpiredData" class="section detail">

    ### ignoreExpiredData

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">ignoreExpiredData</span>

    </div>

    <div class="block">

    A flag indicating whether expired data should be ignored until
    refreshed. Default value is false .

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache)"
    class="section detail">

    ### RasterDataSourceConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSourceConfiguration</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [RasterDataSourceConfiguration.Provider](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource") provider,
    @NonNull
    [RasterDataSourceConfiguration.Cache](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource") cache)</span>

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

  - <div id="<init>(java.lang.String,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Provider,com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache,boolean)"
    class="section detail">

    ### RasterDataSourceConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSourceConfiguration</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [RasterDataSourceConfiguration.Provider](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource") provider,
    @NonNull
    [RasterDataSourceConfiguration.Cache](sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource") cache,
    boolean ignoreExpiredData)</span>

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

    A flag indicating whether expired data should be ignored until
    refreshed. Default value is `false`.

    </div>

  </div>

</div>

