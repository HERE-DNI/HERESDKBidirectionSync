---
title: "TextQuery.Area (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-textquery-area"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-search-package-summary">com.here.sdk.search</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.search.TextQuery.Area → com.here.sdk.search.TextQuery.Area

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-explore-com-here-sdk-search-textquery" title="class in com.here.sdk.search">TextQuery</a>

<div class="type-signature">

<span class="modifiers">public static final class </span><span class="element-name type-name-label">TextQuery.Area</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Area to perform search on.

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

  `final `<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-textquery-area#areaCenter" class="member-name-link"><code>areaCenter</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Geographic coordinates of the center around which to provide the most relevant places.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-textquery-area#boxArea" class="member-name-link"><code>boxArea</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Geographic rectangle area in which to provide the most relevant places.

  </div>

  </div>

  <div class="col-first even-row-color">

  `final `<a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">`GeoCircle`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-textquery-area#circleArea" class="member-name-link"><code>circleArea</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Geographic circle area in which to provide the most relevant places.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">`GeoCorridor`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-textquery-area#corridorArea" class="member-name-link"><code>corridorArea</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Geographic corridor area in which to provide the most relevant places.

  </div>

  </div>

  <div class="col-first even-row-color">

  `final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">`CountryCode`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-textquery-area#countries" class="member-name-link"><code>countries</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A list of countries that the query is applied in.

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

      Area ( GeoBox boxArea)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Area ( GeoCircle circleArea)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      Area ( GeoCoordinates areaCenter)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      Area ( GeoCorridor corridorArea, GeoCoordinates areaCenter)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      Area ( List < CountryCode > countries, GeoCoordinates areaCenter)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a new instance of this class from provided parameters.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-areaCenter" class="section detail">

    ### areaCenter

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">areaCenter</span>

    </div>

    <div class="block">

    Geographic coordinates of the center around which to provide the most relevant places. For Offline Search, one of areaCenter , boxArea and circleArea has to be set, otherwise it will result in SearchError.INVALID_AREA .

    </div>

    </div>

  - <div id="sdk-for-android-explore-boxArea" class="section detail">

    ### boxArea

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">boxArea</span>

    </div>

    <div class="block">

    Geographic rectangle area in which to provide the most relevant places. For Offline Search, one of areaCenter , boxArea and circleArea has to be set, otherwise it will result in SearchError.INVALID_AREA . Also, for Offline Search, search in a given GeoBox restricts the results to only POIs.

    </div>

    </div>

  - <div id="sdk-for-android-explore-circleArea" class="section detail">

    ### circleArea

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a></span> <span class="element-name">circleArea</span>

    </div>

    <div class="block">

    Geographic circle area in which to provide the most relevant places. For Offline Search, one of areaCenter , boxArea and circleArea has to be set, otherwise it will result in SearchError.INVALID_AREA . Also, for Offline Search, search in a given GeoCircle restricts the results to only POIs.

    </div>

    </div>

  - <div id="sdk-for-android-explore-corridorArea" class="section detail">

    ### corridorArea

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></span> <span class="element-name">corridorArea</span>

    </div>

    <div class="block">

    Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query. When used with SearchEngine, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity. When corridorArea is provided, areaCenter has to be within it, otherwise areaCenter is ignored when searching. For Offline Search, search in a given GeoCorridor restricts the results to only POIs.

    </div>

    </div>

  - <div id="sdk-for-android-explore-countries" class="section detail">

    ### countries

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>\></span> <span class="element-name">countries</span>

    </div>

    <div class="block">

    A list of countries that the query is applied in. Not supported in OfflineSearchEngine (which is only available for the Navigate license).

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `areaCenter` -

    Geographic coordinates of the center around which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoBox" class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters. For Offline Search, search in a given GeoBox restricts the results to only POIs.

    </div>

    Parameters:  
    `boxArea` -

    Geographic rectangle area in which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoCircle" class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters. For Offline Search, search in a given GeoCircle restricts the results to only POIs.

    </div>

    Parameters:  
    `circleArea` -

    Geographic circle area in which to provide the most relevant places.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoCorridor-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea, @NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters. The given corridor and center define the area that will be used in the search query. When used with SearchEngine, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity. The area center has to be within the corridor, otherwise it is ignored. For Offline Search, search in a given GeoCorridor restricts the results to only POIs.

    </div>

    Parameters:  
    `corridorArea` -

    Geographic corridor area in which to provide the most relevant places.

    `areaCenter` -

    Geographic coordinates of the prioritized area center.

    </div>

  - <div id="sdk-for-android-explore-init-java-util-List-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a>\> countries, @NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters. The given list of countries and center define the area that will be used in the search query.

    </div>

    Parameters:  
    `countries` -

    A list of countries that the query is applied in.

    `areaCenter` -

    Geographic coordinates of the prioritized area center.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

