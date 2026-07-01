---
title: "AddressQuery (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-addressquery"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.AddressQuery

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">AddressQuery</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify an address query. A query can consist of parts of
an address or full addresses, optionally comma separated. AddressQuery
should only be used to search for parts of the address, excluding the
POI name. For example, "Invalidenstraße 116, Berlin, Germany" is
appropriate, whereas "HERE, Invalidenstraße 116, Berlin, Germany" is
not. To be able to include the POI name, use TextQuery instead.
SearchOptions.languageCode specifies the language of the query and
determines the preferred language of the results.

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
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-addressquery#areaCenter"
  class="member-name-link"><code>areaCenter</code></a></td>
  <td><div class="block">
  Geographical coordinates of the center around which to provide the most
  relevant places.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-countrycode"
  title="enum class in com.here.sdk.core"><code>CountryCode</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-addressquery#countries"
  class="member-name-link"><code>countries</code></a></td>
  <td><div class="block">
  A list of countries that the query is applied in.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-addressquery#query"
  class="member-name-link"><code>query</code></a></td>
  <td><div class="block">
  Desired address query to search.
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
  <td><pre><code>AddressQuery(String query)</code></pre></td>
  <td><div class="block">
  Constructs an AddressQuery from the provided text query.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>AddressQuery(String query,
   GeoCoordinates areaCenter)</code></pre></td>
  <td><div class="block">
  Constructs an AddressQuery from the provided text query and geographical
  coordinates.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>AddressQuery(String query,
   GeoCoordinates areaCenter,
   List&lt;CountryCode&gt; countries)</code></pre></td>
  <td><div class="block">
  Constructs an AddressQuery from the provided text query, geographical
  coordinates and the list of countries the query is applied in.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
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

  - <div id="query" class="section detail">

    ### query

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">query</span>

    </div>

    <div class="block">

    Desired address query to search.

    </div>

    </div>

  - <div id="areaCenter" class="section detail">

    ### areaCenter

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">areaCenter</span>

    </div>

    <div class="block">

    Geographical coordinates of the center around which to provide the
    most relevant places. For Offline Search null value will result in
    SearchError.INVALID_AREA

    </div>

    </div>

  - <div id="countries" class="section detail">

    ### countries

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[CountryCode](sdk-for-android-explore-com-here-sdk-core-countrycode "enum class in com.here.sdk.core")></span> <span class="element-name">countries</span>

    </div>

    <div class="block">

    A list of countries that the query is applied in. Not supported in
    OfflineSearchEngine (only available for the Navigate license).

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.String,com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### AddressQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AddressQuery</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> query,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") areaCenter)</span>

    </div>

    <div class="block">

    Constructs an AddressQuery from the provided text query and
    geographical coordinates.

    </div>

    Parameters:  
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographical coordinates of the center around which to provide the
    most relevant places.

    </div>

  - <div id="<init>(java.lang.String,com.here.sdk.core.GeoCoordinates,java.util.List)"
    class="section detail">

    ### AddressQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AddressQuery</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> query,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") areaCenter,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[CountryCode](sdk-for-android-explore-com-here-sdk-core-countrycode "enum class in com.here.sdk.core")> countries)</span>

    </div>

    <div class="block">

    Constructs an AddressQuery from the provided text query,
    geographical coordinates and the list of countries the query is
    applied in.

    </div>

    Parameters:  
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographical coordinates of the center around which to provide the
    most relevant places.

    `countries` -

    A list of countries that the query is applied in.

    </div>

  - <div id="<init>(java.lang.String)" class="section detail">

    ### AddressQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AddressQuery</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> query)</span>

    </div>

    <div class="block">

    Constructs an AddressQuery from the provided text query. Not
    supported in OfflineSearchEngine (only available for the Navigate
    license).

    </div>

    Parameters:  
    `query` -

    Desired query to search.

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

  </div>

</div>

