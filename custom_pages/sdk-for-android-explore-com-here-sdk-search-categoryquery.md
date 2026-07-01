---
title: "CategoryQuery (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-categoryquery"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.CategoryQuery

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">CategoryQuery</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify a query by categories.

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
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area"
  class="type-name-link"
  title="class in com.here.sdk.search"><code>CategoryQuery.Area</code></a></td>
  <td><div class="block">
  Area to perform search on.
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
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area"
  title="class in com.here.sdk.search"><code>CategoryQuery.Area</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#area"
  class="member-name-link"><code>area</code></a></td>
  <td><div class="block">
  Area in which to provide the most relevant places.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placecategory"
  title="class in com.here.sdk.search"><code>PlaceCategory</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#categories"
  class="member-name-link"><code>categories</code></a></td>
  <td><div class="block">
  List of categories to be included.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placecategory"
  title="class in com.here.sdk.search"><code>PlaceCategory</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#excludeCategories"
  class="member-name-link"><code>excludeCategories</code></a></td>
  <td><div class="block">
  List of categories and subcategories to be excluded.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placechain"
  title="class in com.here.sdk.search"><code>PlaceChain</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#excludeChains"
  class="member-name-link"><code>excludeChains</code></a></td>
  <td><div class="block">
  List of chains to be excluded.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placefoodtype"
  title="class in com.here.sdk.search"><code>PlaceFoodType</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#excludeFoodTypes"
  class="member-name-link"><code>excludeFoodTypes</code></a></td>
  <td><div class="block">
  List of food types to be excluded.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#filter"
  class="member-name-link"><code>filter</code></a></td>
  <td><div class="block">
  Full-text filter on POI names/titles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placechain"
  title="class in com.here.sdk.search"><code>PlaceChain</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#includeChains"
  class="member-name-link"><code>includeChains</code></a></td>
  <td><div class="block">
  List of chains to be included.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-placefoodtype"
  title="class in com.here.sdk.search"><code>PlaceFoodType</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#includeFoodTypes"
  class="member-name-link"><code>includeFoodTypes</code></a></td>
  <td><div class="block">
  List of food types to be included.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-placefilter"
  title="class in com.here.sdk.search"><code>PlaceFilter</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery#placeFilter"
  class="member-name-link"><code>placeFilter</code></a></td>
  <td><div class="block">
  The filter options to specify a place in query.
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
  <td><pre><code>CategoryQuery(PlaceCategory category,
   CategoryQuery.Area area)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>CategoryQuery(PlaceCategory category,
   String filter,
   CategoryQuery.Area area)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>CategoryQuery(List&lt;PlaceCategory&gt; categories,
   CategoryQuery.Area area)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>CategoryQuery(List&lt;PlaceCategory&gt; categories,
   String filter,
   CategoryQuery.Area area)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
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

  - <div id="categories" class="section detail">

    ### categories

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")></span> <span class="element-name">categories</span>

    </div>

    <div class="block">

    List of categories to be included. A place can be assigned multiple
    categories. If any of them is in CategoryQuery.categories , but none
    are in CategoryQuery.excludeCategories , that place will be included
    in the response.

    </div>

    </div>

  - <div id="excludeCategories" class="section detail">

    ### excludeCategories

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")></span> <span class="element-name">excludeCategories</span>

    </div>

    <div class="block">

    List of categories and subcategories to be excluded. A place can be
    assigned multiple categories. If any of them is in
    CategoryQuery.excludeCategories , that place will not be included in
    the response, regardless of whether any of its assigned categories
    have been included in CategoryQuery.categories . In short, an
    exclusion will always win over an inclusion. This is especially
    useful for excluding specific subcategories from the main category.

    </div>

    </div>

  - <div id="includeChains" class="section detail">

    ### includeChains

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceChain](sdk-for-android-explore-com-here-sdk-search-placechain "class in com.here.sdk.search")></span> <span class="element-name">includeChains</span>

    </div>

    <div class="block">

    List of chains to be included. A place can be assigned multiple
    chains. If any of them is in CategoryQuery.includeChains , but none
    are in CategoryQuery.excludeChains , that place will be included in
    the response.

    </div>

    </div>

  - <div id="excludeChains" class="section detail">

    ### excludeChains

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceChain](sdk-for-android-explore-com-here-sdk-search-placechain "class in com.here.sdk.search")></span> <span class="element-name">excludeChains</span>

    </div>

    <div class="block">

    List of chains to be excluded. A place can be assigned multiple
    chains. If any of them is in CategoryQuery.excludeChains , that
    place will not be included in the response, regardless of whether
    any of its assigned chains have been included in
    CategoryQuery.includeChains . In short, an exclusion will always win
    over an inclusion.

    </div>

    </div>

  - <div id="includeFoodTypes" class="section detail">

    ### includeFoodTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceFoodType](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")></span> <span class="element-name">includeFoodTypes</span>

    </div>

    <div class="block">

    List of food types to be included. A place can be assigned multiple
    food types. If any of them is in CategoryQuery.includeFoodTypes ,
    but none are in CategoryQuery.excludeFoodTypes , that place will be
    included in the response.

    </div>

    </div>

  - <div id="excludeFoodTypes" class="section detail">

    ### excludeFoodTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceFoodType](sdk-for-android-explore-com-here-sdk-search-placefoodtype "class in com.here.sdk.search")></span> <span class="element-name">excludeFoodTypes</span>

    </div>

    <div class="block">

    List of food types to be excluded. A place can be assigned multiple
    food types. If any of them is in CategoryQuery.excludeFoodTypes ,
    that place will not be included in the response, regardless of
    whether any of its assigned food types have been included in
    CategoryQuery.includeFoodTypes . In short, an exclusion will always
    win over an inclusion.

    </div>

    </div>

  - <div id="filter" class="section detail">

    ### filter

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">filter</span>

    </div>

    <div class="block">

    Full-text filter on POI names/titles. Results with a partial match
    are included in the response. By default the value is set to null
    and results will be based on other parameters provided.

    </div>

    </div>

  - <div id="placeFilter" class="section detail">

    ### placeFilter

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PlaceFilter](sdk-for-android-explore-com-here-sdk-search-placefilter "class in com.here.sdk.search")</span> <span class="element-name">placeFilter</span>

    </div>

    <div class="block">

    The filter options to specify a place in query. Consists of fuel and
    truck options.

    </div>

    </div>

  - <div id="area" class="section detail">

    ### area

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[CategoryQuery.Area](sdk-for-android-explore-com-here-sdk-search-categoryquery-area "class in com.here.sdk.search")</span> <span class="element-name">area</span>

    </div>

    <div class="block">

    Area in which to provide the most relevant places.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.search.PlaceCategory,com.here.sdk.search.CategoryQuery.Area)"
    class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><span class="parameters">(@NonNull
    [PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search") category,
    @NonNull
    [CategoryQuery.Area](sdk-for-android-explore-com-here-sdk-search-categoryquery-area "class in com.here.sdk.search") area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `category` -

    Category for query

    `area` -

    Area in which to provide the most relevant places.

    </div>

  - <div id="<init>(java.util.List,com.here.sdk.search.CategoryQuery.Area)"
    class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull
    [CategoryQuery.Area](sdk-for-android-explore-com-here-sdk-search-categoryquery-area "class in com.here.sdk.search") area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `categories` -

    List of categories.

    `area` -

    Area in which to provide the most relevant places.

    </div>

  - <div id="<init>(com.here.sdk.search.PlaceCategory,java.lang.String,com.here.sdk.search.CategoryQuery.Area)"
    class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><span class="parameters">(@NonNull
    [PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search") category,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> filter,
    @NonNull
    [CategoryQuery.Area](sdk-for-android-explore-com-here-sdk-search-categoryquery-area "class in com.here.sdk.search") area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `category` -

    Category for query

    `filter` -

    Full-text filter on POI names/titles. Results with a partial match
    are included in the response.

    `area` -

    Area in which to provide the most relevant places.

    </div>

  - <div id="<init>(java.util.List,java.lang.String,com.here.sdk.search.CategoryQuery.Area)"
    class="section detail">

    ### CategoryQuery

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CategoryQuery</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[PlaceCategory](sdk-for-android-explore-com-here-sdk-search-placecategory "class in com.here.sdk.search")> categories,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> filter,
    @NonNull
    [CategoryQuery.Area](sdk-for-android-explore-com-here-sdk-search-categoryquery-area "class in com.here.sdk.search") area)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `categories` -

    List of categories.

    `filter` -

    Full-text filter on POI names/titles. Results with a partial match
    are included in the response.

    `area` -

    Area in which to provide the most relevant places.

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

