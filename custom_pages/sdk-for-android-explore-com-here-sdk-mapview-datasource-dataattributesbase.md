---
title: "DataAttributesBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbase"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

All Known Implementing Classes:  
[`DataAttributes`](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributes "class in com.here.sdk.mapview.datasource"),
[`DataAttributesAccessor`](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesaccessor "class in com.here.sdk.mapview.datasource")

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">DataAttributesBase</span>

</div>

<div class="block">

Interface for a collection of data attributes. Note: This is a beta
release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation
process.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getAsString(String name)</code></pre></td>
  <td><div class="block">
  Gets the value of an attribute as a string or null if it is not
  contained.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a><code>&gt;</code></td>
  <td><pre><code>getAttributeNames()</code></pre></td>
  <td><div class="block">
  Returns a list of attribute names.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
  class="external-link"
  title="class or interface in java.lang"><code>Boolean</code></a></td>
  <td><pre><code>getBoolean(String name)</code></pre></td>
  <td><div class="block">
  Gets the value of a boolean attribute or null if it is not contained or
  the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><pre><code>getDouble(String name)</code></pre></td>
  <td><div class="block">
  Gets the value of a double precision floating decimal attribute or null
  if it is not contained or the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html"
  class="external-link"
  title="class or interface in java.lang"><code>Float</code></a></td>
  <td><pre><code>getFloat(String name)</code></pre></td>
  <td><div class="block">
  Gets the value of a single precision floating decimal attribute or null
  if it is not contained or the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
  class="external-link"
  title="class or interface in java.lang"><code>Long</code></a></td>
  <td><pre><code>getInt64(String name)</code></pre></td>
  <td><div class="block">
  Gets the value of a 64-bits integer attribute or null if it is not
  contained or the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getString(String name)</code></pre></td>
  <td><div class="block">
  Gets the value of a string attribute or null if it is not contained or
  the type doesn't match.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue"
  title="class in com.here.sdk.mapview.datasource"><code>DataAttributeValue</code></a></td>
  <td><pre><code>getValue(String name)</code></pre></td>
  <td><div class="block">
  Gets the DataAttributeValue or null if it is not contained.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype"
  title="enum class in com.here.sdk.mapview.datasource"><code>DataAttributeValue.ValueType</code></a></td>
  <td><pre><code>getValueType(String name)</code></pre></td>
  <td><div class="block">
  Returns the value type of an attribute or null if it is not contained.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="getAttributeNames()" class="section detail">

    ### getAttributeNames

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>></span> <span class="element-name">getAttributeNames</span>()

    </div>

    <div class="block">

    Returns a list of attribute names.

    </div>

    Returns:  
    The list of attribute names.

    </div>

  - <div id="getValueType(java.lang.String)" class="section detail">

    ### getValueType

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type">[DataAttributeValue.ValueType](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")</span> <span class="element-name">getValueType</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the value type of an attribute or null if it is not
    contained.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value type or `null` if it is not contained.

    </div>

  - <div id="getAsString(java.lang.String)" class="section detail">

    ### getAsString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of an attribute as a string or null if it is not
    contained.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="getString(java.lang.String)" class="section detail">

    ### getString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a string attribute or null if it is not contained
    or the type doesn't match.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="getInt64(java.lang.String)" class="section detail">

    ### getInt64

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
    class="external-link" title="class or interface in java.lang">Long</a></span> <span class="element-name">getInt64</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a 64-bits integer attribute or null if it is not
    contained or the type doesn't match.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="getFloat(java.lang.String)" class="section detail">

    ### getFloat

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html"
    class="external-link" title="class or interface in java.lang">Float</a></span> <span class="element-name">getFloat</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a single precision floating decimal attribute or
    null if it is not contained or the type doesn't match.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="getDouble(java.lang.String)" class="section detail">

    ### getDouble

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDouble</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a double precision floating decimal attribute or
    null if it is not contained or the type doesn't match.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="getBoolean(java.lang.String)" class="section detail">

    ### getBoolean

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
    class="external-link"
    title="class or interface in java.lang">Boolean</a></span> <span class="element-name">getBoolean</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a boolean attribute or null if it is not contained
    or the type doesn't match.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="getValue(java.lang.String)" class="section detail">

    ### getValue

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type">[DataAttributeValue](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue "class in com.here.sdk.mapview.datasource")</span> <span class="element-name">getValue</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the DataAttributeValue or null if it is not contained.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  </div>

</div>

