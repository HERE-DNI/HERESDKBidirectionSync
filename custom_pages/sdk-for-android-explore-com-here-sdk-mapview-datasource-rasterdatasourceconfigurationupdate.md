---
title: "RasterDataSourceConfigurationUpdate (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.sdk.mapview.datasource.RasterDataSourceConfigurationUpdate

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">RasterDataSourceConfigurationUpdate</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Configuration update for a RasterDataSource.

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
  class="external-link"
  title="class or interface in java.lang"><code>Long</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate#cacheDiskSize"
  class="member-name-link"><code>cacheDiskSize</code></a></td>
  <td><div class="block">
  Optional update of the cache disk size, in bytes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
  class="external-link"
  title="class or interface in java.lang"><code>Boolean</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate#ignoreExpiredData"
  class="member-name-link"><code>ignoreExpiredData</code></a></td>
  <td><div class="block">
  Optional update of the flag indicating whether expired data should be
  ignored until refreshed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfigurationupdate#providerHeaders"
  class="member-name-link"><code>providerHeaders</code></a></td>
  <td><div class="block">
  Optional update of the provider headers.
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
  <td><pre><code>RasterDataSourceConfigurationUpdate(Map&lt;String,String&gt; providerHeaders,
   Boolean ignoreExpiredData,
   Long cacheDiskSize)</code></pre></td>
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

  - <div id="providerHeaders" class="section detail">

    ### providerHeaders

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>></span> <span class="element-name">providerHeaders</span>

    </div>

    <div class="block">

    Optional update of the provider headers. The new list replaces the
    current one. When not set, no change is made to the current list.

    </div>

    </div>

  - <div id="ignoreExpiredData" class="section detail">

    ### ignoreExpiredData

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
    class="external-link"
    title="class or interface in java.lang">Boolean</a></span> <span class="element-name">ignoreExpiredData</span>

    </div>

    <div class="block">

    Optional update of the flag indicating whether expired data should
    be ignored until refreshed. When not set, no change is made to the
    current flag state.

    </div>

    </div>

  - <div id="cacheDiskSize" class="section detail">

    ### cacheDiskSize

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a></span> <span class="element-name">cacheDiskSize</span>

    </div>

    <div class="block">

    Optional update of the cache disk size, in bytes. When not set, no
    change is made to the current value.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.util.Map,java.lang.Boolean,java.lang.Long)"
    class="section detail">

    ### RasterDataSourceConfigurationUpdate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RasterDataSourceConfigurationUpdate</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> providerHeaders,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
    class="external-link"
    title="class or interface in java.lang">Boolean</a> ignoreExpiredData,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a> cacheDiskSize)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `providerHeaders` -

    Optional update of the provider headers. The new list replaces the
    current one. When not set, no change is made to the current list.

    `ignoreExpiredData` -

    Optional update of the flag indicating whether expired data should
    be ignored until refreshed. When not set, no change is made to the
    current flag state.

    `cacheDiskSize` -

    Optional update of the cache disk size, in bytes. When not set, no
    change is made to the current value.

    </div>

  </div>

</div>

