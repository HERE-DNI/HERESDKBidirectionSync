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

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">CatalogConfiguration</span>
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

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

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#allowDownload" class="member-name-link"><code>allowDownload</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A flag to indicate if the data for this catalog is allowed to be
  stored in persistent storage for use with offline maps.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#cacheExpirationPeriod" class="member-name-link"><code>cacheExpirationPeriod</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Expiration time in seconds for how long the catalog data is retained
  in the map cache before it is removed.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`DesiredCatalog`](sdk-for-android-explore-com-here-sdk-core-engine-desiredcatalog "class in com.here.sdk.core.engine")

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#catalog" class="member-name-link"><code>catalog</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The identifier for the desired catalog to be accessed on the HERE
  platform.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#patchHrn" class="member-name-link"><code>patchHrn</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Some catalogs may have additional modifications to their data
  contained in an entirely separate catalog, called the patch catalog.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      CatalogConfiguration(DesiredCatalog catalog)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`CatalogConfiguration`](sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration "class in com.here.sdk.core.engine")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      getDefault(CatalogType catalogType)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets the default catalog configuration for the specified catalog type.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-catalog" class="section detail">

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

  - <div id="sdk-for-android-explore-patchHrn" class="section detail">

    ### patchHrn

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">patchHrn</span>

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

  - <div id="sdk-for-android-explore-cacheExpirationPeriod"
    class="section detail">

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

  - <div id="sdk-for-android-explore-allowDownload"
    class="section detail">

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

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.engine.DesiredCatalog)"
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

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-getDefault(com.here.sdk.core.engine.CatalogType)"
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

