---
title: "DataAttributeValue (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.datasource.DataAttributeValue →
com.here.NativeBase → com.here.sdk.mapview.datasource.DataAttributeValue

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">DataAttributeValue</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Encapsulates a data attribute value. Supports basic types and arrays of
basic types. Note: This is a beta release of this feature, so there
could be a few bugs and unexpected behavior. Related APIs may change for
new releases without a deprecation process.

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
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview.datasource"><code>DataAttributeValue.ValueType</code></a></td>
  <td><div class="block">
  Supported types of the data attribute values.
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
  <td><pre><code>DataAttributeValue(boolean value)</code></pre></td>
  <td><div class="block">
  Creates a boolean data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>DataAttributeValue(double value)</code></pre></td>
  <td><div class="block">
  Creates a double precision floating decimal data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>DataAttributeValue(float value)</code></pre></td>
  <td><div class="block">
  Creates a single precision floating decimal data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>DataAttributeValue(long value)</code></pre></td>
  <td><div class="block">
  Creates a 64-bit integer data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>DataAttributeValue(Color value)</code></pre></td>
  <td><div class="block">
  Creates a color data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>DataAttributeValue(String value)</code></pre></td>
  <td><div class="block">
  Creates a string data attribute value.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>DataAttributeValue(List&lt;DataAttributeValue&gt; value)</code></pre></td>
  <td><div class="block">
  Creates an aggregated data attribute value.
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributeValue</code></a><code>&gt;</code></td>
  <td><pre><code>getArray()</code></pre></td>
  <td><div class="block">
  Gets the array value or null if the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getAsString()</code></pre></td>
  <td><div class="block">
  Returns a string representation of the contained value.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
  class="external-link"
  title="class or interface in java.lang"><code>Boolean</code></a></td>
  <td><pre><code>getBoolean()</code></pre></td>
  <td><div class="block">
  Gets the boolean value or null if the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><pre><code>getColor()</code></pre></td>
  <td><div class="block">
  Gets the color value or null if the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><pre><code>getDouble()</code></pre></td>
  <td><div class="block">
  Gets the double precision floating decimal value or null if the type
  doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html"
  class="external-link"
  title="class or interface in java.lang"><code>Float</code></a></td>
  <td><pre><code>getFloat()</code></pre></td>
  <td><div class="block">
  Gets the single precision floating decimal value or null if the type
  doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
  class="external-link"
  title="class or interface in java.lang"><code>Long</code></a></td>
  <td><pre><code>getInt64()</code></pre></td>
  <td><div class="block">
  Gets 64-bits integer value or null if the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getString()</code></pre></td>
  <td><div class="block">
  Gets the string value or null if the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype"
  title="enum class in com.here.sdk.mapview.datasource"><code>DataAttributeValue.ValueType</code></a></td>
  <td><pre><code>getType()</code></pre></td>
  <td><div class="block">
  Returns the type of the value.
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

  - <div id="<init>(java.lang.String)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Creates a string data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  - <div id="<init>(long)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(long value)</span>

    </div>

    <div class="block">

    Creates a 64-bit integer data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  - <div id="<init>(float)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(float value)</span>

    </div>

    <div class="block">

    Creates a single precision floating decimal data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  - <div id="<init>(double)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Creates a double precision floating decimal data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  - <div id="<init>(boolean)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Creates a boolean data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  - <div id="<init>(com.here.sdk.core.Color)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(@NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") value)</span>

    </div>

    <div class="block">

    Creates a color data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  - <div id="<init>(java.util.List)" class="section detail">

    ### DataAttributeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DataAttributeValue</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[DataAttributeValue](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue "class in com.here.sdk.mapview.datasource")> value)</span>

    </div>

    <div class="block">

    Creates an aggregated data attribute value.

    </div>

    Parameters:  
    `value` -

    Attribute value.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="getType()" class="section detail">

    ### getType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[DataAttributeValue.ValueType](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">getType</span>()

    </div>

    <div class="block">

    Returns the type of the value.

    </div>

    Returns:  
    The type of the value.

    </div>

  - <div id="getString()" class="section detail">

    ### getString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span>()

    </div>

    <div class="block">

    Gets the string value or null if the type doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getInt64()" class="section detail">

    ### getInt64

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a></span> <span class="element-name">getInt64</span>()

    </div>

    <div class="block">

    Gets 64-bits integer value or null if the type doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getFloat()" class="section detail">

    ### getFloat

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html"
    class="external-link" title="class or interface in java.lang">Float</a></span> <span class="element-name">getFloat</span>()

    </div>

    <div class="block">

    Gets the single precision floating decimal value or null if the type
    doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getDouble()" class="section detail">

    ### getDouble

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDouble</span>()

    </div>

    <div class="block">

    Gets the double precision floating decimal value or null if the type
    doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getBoolean()" class="section detail">

    ### getBoolean

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
    class="external-link"
    title="class or interface in java.lang">Boolean</a></span> <span class="element-name">getBoolean</span>()

    </div>

    <div class="block">

    Gets the boolean value or null if the type doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getColor()" class="section detail">

    ### getColor

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getColor</span>()

    </div>

    <div class="block">

    Gets the color value or null if the type doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getArray()" class="section detail">

    ### getArray

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[DataAttributeValue](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue "class in com.here.sdk.mapview.datasource")></span> <span class="element-name">getArray</span>()

    </div>

    <div class="block">

    Gets the array value or null if the type doesn't match.

    </div>

    Returns:  
    Attribute value.

    </div>

  - <div id="getAsString()" class="section detail">

    ### getAsString

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span>()

    </div>

    <div class="block">

    Returns a string representation of the contained value.

    </div>

    Returns:  
    Attribute value.

    </div>

  </div>

</div>

