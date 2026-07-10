---
title: "AddressQuery (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-addressquery"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.search.AddressQuery → com.here.sdk.search.AddressQuery

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AddressQuery</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify an address query. A query can consist of parts of an address or full addresses, optionally comma separated. AddressQuery should only be used to search for parts of the address, excluding the POI name. For example, "Invalidenstraße 116, Berlin, Germany" is appropriate, whereas "HERE, Invalidenstraße 116, Berlin, Germany" is not. To be able to include the POI name, use TextQuery instead. SearchOptions.languageCode specifies the language of the query and determines the preferred language of the results.

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

  `final `<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery#areaCenter" class="member-name-link"><code>areaCenter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Geographical coordinates of the center around which to provide the most relevant places.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">`CountryCode`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery#countries" class="member-name-link"><code>countries</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A list of countries that the query is applied in.

  </div>

  </div>

  <div class="col-first even-row-color">

  `final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-search-addressquery#query" class="member-name-link"><code>query</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Desired address query to search.

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

      AddressQuery ( String query)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an AddressQuery from the provided text query.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      AddressQuery ( String query, GeoCoordinates areaCenter)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs an AddressQuery from the provided text query and geographical coordinates.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      AddressQuery ( String query, GeoCoordinates areaCenter, List < CountryCode > countries)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-query" class="section detail">

    ### query

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">query</span>

    </div>

    <div class="block">

    Desired address query to search.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-areaCenter" class="section detail">

    ### areaCenter

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">areaCenter</span>

    </div>

    <div class="block">

    Geographical coordinates of the center around which to provide the most relevant places. For Offline Search null value will result in SearchError.INVALID_AREA

    </div>

    </div>

  - <div id="sdk-for-android-navigate-countries" class="section detail">

    ### countries

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>\></span> <span class="element-name">countries</span>

    </div>

    <div class="block">

    A list of countries that the query is applied in. Not supported in OfflineSearchEngine (only available for the Navigate license).

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-lang-String-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### AddressQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AddressQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span>

    </div>

    <div class="block">

    Constructs an AddressQuery from the provided text query and geographical coordinates.

    </div>

    Parameters:  
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographical coordinates of the center around which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String-com-here-sdk-core-GeoCoordinates-java-util-List" class="section detail">

    ### AddressQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AddressQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> query, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>\> countries)</span>

    </div>

    <div class="block">

    Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.

    </div>

    Parameters:  
    `query` -

    Desired query to search.

    `areaCenter` -

    Geographical coordinates of the center around which to provide the most relevant places.

    `countries` -

    A list of countries that the query is applied in.

    </div>

  - <div id="sdk-for-android-navigate-init-java-lang-String" class="section detail">

    ### AddressQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AddressQuery</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> query)</span>

    </div>

    <div class="block">

    Constructs an AddressQuery from the provided text query. Not supported in OfflineSearchEngine (only available for the Navigate license).

    </div>

    Parameters:  
    `query` -

    Desired query to search.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

