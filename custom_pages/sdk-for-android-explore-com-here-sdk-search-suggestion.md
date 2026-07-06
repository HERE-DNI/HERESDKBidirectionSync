---
title: "Suggestion (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-suggestion"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.search.Suggestion →
com.here.NativeBase → com.here.sdk.search.Suggestion

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Suggestion</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Suggestion is meant to provide relevant suggestions to partial queries,
like "restaur", "starbu", "eiffel". Represents a relevant response to
user queries. Suggestions (please check SuggestionType ) are either:
Place: SuggestionType.PLACE Query: SuggestionType.CHAIN or
SuggestionType.CATEGORY With "Place" you get data for a concrete place
in the world. With "Query" something to follow-up, a way to perform more
focused search.

</div>

</div>

<div class="section summary">

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

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a>`<`[`HighlightType`](sdk-for-android-explore-com-here-sdk-search-highlighttype "enum class in com.here.sdk.search")`,`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`IndexRange`](sdk-for-android-explore-com-here-sdk-search-indexrange "class in com.here.sdk.search")`>>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getHighlights()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The text slices matching the input query.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getHref()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the direct link for Discover query.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getId()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the suggested item id.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Place`](sdk-for-android-explore-com-here-sdk-search-place "class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPlace()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the suggested place item.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTitle()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the localized title for the suggestion.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`SuggestionType`](sdk-for-android-explore-com-here-sdk-search-suggestiontype "enum class in com.here.sdk.search")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getType()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the type of suggestion.

  </div>

  </div>

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

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getHighlights()"
    class="section detail">

    ### getHighlights

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<[HighlightType](sdk-for-android-explore-com-here-sdk-search-highlighttype "enum class in com.here.sdk.search"),<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[IndexRange](sdk-for-android-explore-com-here-sdk-search-indexrange "class in com.here.sdk.search")\>\></span> <span class="element-name">getHighlights</span>()

    </div>

    <div class="block">

    The text slices matching the input query.

    </div>

    Returns:  
    Associated container where
    [`HighlightType`](sdk-for-android-explore-com-here-sdk-search-highlighttype "enum class in com.here.sdk.search")
    is a key and list of
    [`IndexRange`](sdk-for-android-explore-com-here-sdk-search-indexrange "class in com.here.sdk.search")
    value.

    </div>

  - <div id="sdk-for-android-explore-getTitle()" class="section detail">

    ### getTitle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()

    </div>

    <div class="block">

    Gets the localized title for the suggestion.

    </div>

    Returns:  
    The localized title for the suggestion.

    </div>

  - <div id="sdk-for-android-explore-getType()" class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[SuggestionType](sdk-for-android-explore-com-here-sdk-search-suggestiontype "enum class in com.here.sdk.search")</span> <span class="element-name">getType</span>()

    </div>

    <div class="block">

    Gets the type of suggestion.

    </div>

    Returns:  
    Type of the suggestion.

    </div>

  - <div id="sdk-for-android-explore-getPlace()" class="section detail">

    ### getPlace

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Place](sdk-for-android-explore-com-here-sdk-search-place "class in com.here.sdk.search")</span> <span class="element-name">getPlace</span>()

    </div>

    <div class="block">

    Gets the suggested place item. Available only for
    SuggestionType.PLACE .

    </div>

    Returns:  
    The suggested place.

    </div>

  - <div id="sdk-for-android-explore-getId()" class="section detail">

    ### getId

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()

    </div>

    <div class="block">

    Gets the suggested item id. For online search, suggestion of type
    SuggestionType.PLACE will have Suggestion.id same as Place.id. For
    offline search, only suggestion of type SuggestionType.CHAIN , will
    have this property filled with identifier number of an associated
    chain. For example, the chain ID "8778" corresponds to the chain
    name "ABC Shop". For other types, SuggestionType.PLACE and
    SuggestionType.CATEGORY this property will be null.

    </div>

    Returns:  
    The unique id of suggested item. It can be used to query further
    information.

    </div>

  - <div id="sdk-for-android-explore-getHref()" class="section detail">

    ### getHref

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getHref</span>()

    </div>

    <div class="block">

    Gets the direct link for Discover query. Available only for
    SuggestionType.CHAIN and SuggestionType.CATEGORY . This is not
    supported in offline search.

    </div>

    Returns:  
    Direct URL for precise query.

    </div>

  </div>

</div>

