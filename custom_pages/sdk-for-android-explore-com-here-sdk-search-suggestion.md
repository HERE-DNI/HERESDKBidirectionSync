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

<div id="class-description" class="section class-description">

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
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-highlighttype"
  title="enum class in com.here.sdk.search"><code>HighlightType</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-indexrange"
  title="class in com.here.sdk.search"><code>IndexRange</code></a><code>&gt;&gt;</code></td>
  <td><pre><code>getHighlights()</code></pre></td>
  <td><div class="block">
  The text slices matching the input query.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getHref()</code></pre></td>
  <td><div class="block">
  Gets the direct link for Discover query.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getId()</code></pre></td>
  <td><div class="block">
  Gets the suggested item id.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-place"
  title="class in com.here.sdk.search"><code>Place</code></a></td>
  <td><pre><code>getPlace()</code></pre></td>
  <td><div class="block">
  Gets the suggested place item.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getTitle()</code></pre></td>
  <td><div class="block">
  Gets the localized title for the suggestion.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-suggestiontype"
  title="enum class in com.here.sdk.search"><code>SuggestionType</code></a></td>
  <td><pre><code>getType()</code></pre></td>
  <td><div class="block">
  Gets the type of suggestion.
  </div></td>
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

- <div id="method-detail" class="section method-details">

  - <div id="getHighlights()" class="section detail">

    ### getHighlights

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><[HighlightType](sdk-for-android-explore-com-here-sdk-search-highlighttype "enum class in com.here.sdk.search"),<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[IndexRange](sdk-for-android-explore-com-here-sdk-search-indexrange "class in com.here.sdk.search")>></span> <span class="element-name">getHighlights</span>()

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

  - <div id="getTitle()" class="section detail">

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

  - <div id="getType()" class="section detail">

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

  - <div id="getPlace()" class="section detail">

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

  - <div id="getId()" class="section detail">

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

  - <div id="getHref()" class="section detail">

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

