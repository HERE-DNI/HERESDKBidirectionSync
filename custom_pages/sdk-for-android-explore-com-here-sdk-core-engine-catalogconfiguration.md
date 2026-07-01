---
title: "CatalogConfiguration (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.engine.CatalogConfiguration

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">CatalogConfiguration</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Using this class you can configure in the SDKOptions , how the
SDKNativeEngine should access, use and store the data for the desired
catalog. Using this class, you can access default catalogs on the HERE
platform and also custom catalogs such as for self-hosted or BYOD (bring
your own data) use cases. For information on how the user can identify a
catalog on the HERE platform, see DesiredCatalog For further information
about catalogs and related concepts see CatalogIdentifier . Note: This
API is only applicable for the Navigate license.

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
  <td><code>boolean</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#allowDownload"
  class="member-name-link"><code>allowDownload</code></a></td>
  <td><div class="block">
  A flag to indicate if the data for this catalog is allowed to be stored
  in persistent storage for use with offline maps.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-time-duration"
  title="class in com.here.time"><code>Duration</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#cacheExpirationPeriod"
  class="member-name-link"><code>cacheExpirationPeriod</code></a></td>
  <td><div class="block">
  Expiration time in seconds for how long the catalog data is retained in
  the map cache before it is removed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog"
  title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#catalog"
  class="member-name-link"><code>catalog</code></a></td>
  <td><div class="block">
  The identifier for the desired catalog to be accessed on the HERE
  platform.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#patchHrn"
  class="member-name-link"><code>patchHrn</code></a></td>
  <td><div class="block">
  Some catalogs may have additional modifications to their data contained
  in an entirely separate catalog, called the patch catalog.
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
  <td><pre><code>CatalogConfiguration(DesiredCatalog catalog)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration"
  title="class in com.here.sdk.core.engine"><code>CatalogConfiguration</code></a></td>
  <td><pre><code>getDefault(CatalogType catalogType)</code></pre></td>
  <td><div class="block">
  Gets the default catalog configuration for the specified catalog type.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
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

  - <div id="catalog" class="section detail">

    ### catalog

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DesiredCatalog](sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog "class in com.here.sdk.core.engine")</span> <span class="element-name">catalog</span>

    </div>

    <div class="block">

    The identifier for the desired catalog to be accessed on the HERE
    platform. See DesiredCatalog .

    </div>

    </div>

  - <div id="patchHrn" class="section detail">

    ### patchHrn

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">patchHrn</span>

    </div>

    <div class="block">

    Some catalogs may have additional modifications to their data
    contained in an entirely separate catalog, called the patch catalog.
    This field indicates the HERE Resource Name (HRN) for the patch
    catalog. When this field is present, the catalog's data as
    referenced by catalog is merged with data from the patch catalog. If
    this field is null , then incremental updates are disabled.

    </div>

    </div>

  - <div id="cacheExpirationPeriod" class="section detail">

    ### cacheExpirationPeriod

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">cacheExpirationPeriod</span>

    </div>

    <div class="block">

    Expiration time in seconds for how long the catalog data is retained
    in the map cache before it is removed. Cache path is specified by
    SDKOptions.cachePath . If not set, the cache will be deleted on a
    Least Recently Used (LRU) basis.

    </div>

    </div>

  - <div id="allowDownload" class="section detail">

    ### allowDownload

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">allowDownload</span>

    </div>

    <div class="block">

    A flag to indicate if the data for this catalog is allowed to be
    stored in persistent storage for use with offline maps. The storage
    path is specified in SDKOptions.persistentMapStoragePath . If set to
    false, the data is not stored in persistent storage and is only
    retained in the cache for a limited time (see cacheExpirationPeriod
    ). Defaults to true .

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.engine.DesiredCatalog)"
    class="section detail">

    ### CatalogConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CatalogConfiguration</span><span class="parameters">(@NonNull
    [DesiredCatalog](sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog "class in com.here.sdk.core.engine") catalog)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `catalog` -

    The identifier for the desired catalog to be accessed on the HERE
    platform. See
    [`DesiredCatalog`](sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog "class in com.here.sdk.core.engine").

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="getDefault(com.here.sdk.core.engine.CatalogType)"
    class="section detail">

    ### getDefault

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[CatalogConfiguration](sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration "class in com.here.sdk.core.engine")</span> <span class="element-name">getDefault</span><span class="parameters">(@NonNull
    [CatalogType](sdk-for-android-explore-com-here-sdk-core-engine-catalogtype "enum class in com.here.sdk.core.engine") catalogType)</span>

    </div>

    <div class="block">

    Gets the default catalog configuration for the specified catalog
    type. It uses the catalog version that was the latest at the time
    when the HERE SDK was built.

    </div>

    Parameters:  
    `catalogType` -

    Catalog type

    Returns:  
    Instance of
    [`CatalogConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration "class in com.here.sdk.core.engine").

    </div>

  </div>

</div>

