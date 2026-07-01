---
title: "DataAttributesBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.DataAttributesBuilder
→ com.here.NativeBase →
com.here.sdk.mapview.datasource.DataAttributesBuilder

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">DataAttributesBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Data attributes collection builder. Note: This is a beta release of this
feature, so there could be a few bugs and unexpected behavior. Related
APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">

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
  <td><pre><code>DataAttributesBuilder()</code></pre></td>
  <td><div class="block">
  Creates a data attributes builder instance.
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
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributes</code></a></td>
  <td><pre><code>build()</code></pre></td>
  <td><div class="block">
  Builds instance of DataAttributes.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesBuilder</code></a></td>
  <td><pre><code>with(String name,
   boolean value)</code></pre></td>
  <td><div class="block">
  Configures the builder to add the given attribute.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesBuilder</code></a></td>
  <td><pre><code>with(String name,
   double value)</code></pre></td>
  <td><div class="block">
  Configures the builder to add the given attribute.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesBuilder</code></a></td>
  <td><pre><code>with(String name,
   float value)</code></pre></td>
  <td><div class="block">
  Configures the builder to add the given attribute.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesBuilder</code></a></td>
  <td><pre><code>with(String name,
   long value)</code></pre></td>
  <td><div class="block">
  Configures the builder to add the given attribute.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesBuilder</code></a></td>
  <td><pre><code>with(String name,
   DataAttributeValue value)</code></pre></td>
  <td><div class="block">
  Configures the builder to add the given attribute.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributesBuilder</code></a></td>
  <td><pre><code>with(String name,
   String value)</code></pre></td>
  <td><div class="block">
  Configures the builder to add the given attribute.
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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### DataAttributesBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributesBuilder</span>()

    </div>

    <div class="block">

    Creates a data attributes builder instance.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="with(java.lang.String,java.lang.String)"
    class="section detail">

    ### with

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">with</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Configures the builder to add the given attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:  
    This data attributes builder instance.

    </div>

  - <div id="with(java.lang.String,long)" class="section detail">

    ### with

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">with</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    long value)</span>

    </div>

    <div class="block">

    Configures the builder to add the given attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:  
    This data attributes builder instance.

    </div>

  - <div id="with(java.lang.String,float)" class="section detail">

    ### with

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">with</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    float value)</span>

    </div>

    <div class="block">

    Configures the builder to add the given attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:  
    This data attributes builder instance.

    </div>

  - <div id="with(java.lang.String,double)" class="section detail">

    ### with

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">with</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    double value)</span>

    </div>

    <div class="block">

    Configures the builder to add the given attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:  
    This data attributes builder instance.

    </div>

  - <div id="with(java.lang.String,boolean)" class="section detail">

    ### with

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">with</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    boolean value)</span>

    </div>

    <div class="block">

    Configures the builder to add the given attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:  
    This data attributes builder instance.

    </div>

  - <div id="with(java.lang.String,com.here.sdk.mapview.datasource.DataAttributeValue)"
    class="section detail">

    ### with

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributesBuilder](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbuilder "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">with</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [DataAttributeValue](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue "class in com.here.sdk.mapview.datasource") value)</span>

    </div>

    <div class="block">

    Configures the builder to add the given attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    Returns:  
    This data attributes builder instance.

    </div>

  - <div id="build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributes](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Builds instance of DataAttributes.

    </div>

    Returns:  
    Instance of the data attributes created with the given attributes.

    </div>

  </div>

</div>

