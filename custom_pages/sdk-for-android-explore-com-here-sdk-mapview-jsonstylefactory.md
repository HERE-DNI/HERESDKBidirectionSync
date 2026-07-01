---
title: "JsonStyleFactory (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.JsonStyleFactory →
com.here.NativeBase → com.here.sdk.mapview.JsonStyleFactory

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">JsonStyleFactory</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A factory of Style objects from styles defined in JSON format. For more
details see Custom Layer Style Reference in the documentation. Note:
This is a beta release of this feature, so there could be a few bugs and
unexpected behavior. Related APIs may change for new releases without a
deprecation process.

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
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>JsonStyleFactory.InstantiationErrorCode</code></a></td>
  <td><div class="block">
  Describes reasons for failing to create a Style from a JSON source.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationerrordetails"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>JsonStyleFactory.InstantiationErrorDetails</code></a></td>
  <td><div class="block">
  Describes the reason for failing to create a Style from a JSON source.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>JsonStyleFactory.InstantiationException</code></a></td>
  <td><div class="block">
  Thrown when failing to create a Style from a JSON source.
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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-style"
  title="class in com.here.sdk.mapview"><code>Style</code></a></td>
  <td><pre><code>createFromString(String styleString)</code></pre></td>
  <td><div class="block">
  Creates an instance of Style from a JSON string.
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

  - <div id="createFromString(java.lang.String)" class="section detail">

    ### createFromString

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Style](sdk-for-android-explore-com-here-sdk-mapview-style "class in com.here.sdk.mapview")</span> <span class="element-name">createFromString</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> styleString)</span>
    throws
    <span class="exceptions">[JsonStyleFactory.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates an instance of Style from a JSON string.

    </div>

    Parameters:  
    `styleString` -

    JSON style string.

    Returns:  
    Style instance.

    Throws:  
    [`JsonStyleFactory.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-jsonstylefactory-instantiationexception "class in com.here.sdk.mapview")
    -

    Indicates failure to create
    [`Style`](sdk-for-android-explore-com-here-sdk-mapview-style "class in com.here.sdk.mapview")
    from JSON string.

    </div>

  </div>

</div>

