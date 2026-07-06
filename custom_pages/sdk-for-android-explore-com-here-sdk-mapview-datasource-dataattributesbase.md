---
title: "DataAttributesBase (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributesbase"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getAsString(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the value of an attribute as a string or null if it is not
  contained.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getAttributeNames()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns a list of attribute names.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html"
  class="external-link"
  title="class or interface in java.lang"><code>Boolean</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getBoolean(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the value of a boolean attribute or null if it is not contained
  or the type doesn't match.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getDouble(String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the value of a double precision floating decimal attribute or
  null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html"
  class="external-link"
  title="class or interface in java.lang"><code>Float</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getFloat(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the value of a single precision floating decimal attribute or
  null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html"
  class="external-link"
  title="class or interface in java.lang"><code>Long</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getInt64(String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the value of a 64-bits integer attribute or null if it is not
  contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getString(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the value of a string attribute or null if it is not contained or
  the type doesn't match.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`DataAttributeValue`](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue "class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getValue(String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the DataAttributeValue or null if it is not contained.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`DataAttributeValue.ValueType`](sdk-for-android-explore-com-here-sdk-mapview-datasource-dataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getValueType(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns the value type of an attribute or null if it is not contained.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getAttributeNames()"
    class="section detail">

    ### getAttributeNames

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>></span> <span class="element-name">getAttributeNames</span>()

    </div>

    <div class="block">

    Returns a list of attribute names.

    </div>

    Returns:  
    The list of attribute names.

    </div>

  - <div id="sdk-for-android-explore-getValueType(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getAsString(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getString(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getInt64(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getFloat(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getDouble(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getBoolean(java.lang.String)"
    class="section detail">

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

  - <div id="sdk-for-android-explore-getValue(java.lang.String)"
    class="section detail">

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

