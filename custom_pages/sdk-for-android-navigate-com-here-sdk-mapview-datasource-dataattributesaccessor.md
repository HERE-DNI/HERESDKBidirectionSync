---
title: "DataAttributesAccessor (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesaccessor"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.datasource.DataAttributesAccessor → com.here.NativeBase com.here.sdk.mapview.datasource.DataAttributesAccessor → com.here.sdk.mapview.datasource.DataAttributesAccessor

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">DataAttributesAccessor</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">DataAttributesBase</a></span>

</div>

<div class="block">

Accessor used for manipulating data attributes. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name,
       boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces a boolean attribute.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name,
       double value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces a double precision floating decimal attribute.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name,
       float value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces a single precision floating decimal attribute.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name,
       long value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces a 64-bits integer attribute.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name, Color value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces a color attribute.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name, DataAttributeValue value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces an attribute.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addOrReplace ( String name, String value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds or replaces a string attribute.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAsString ( String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of an attribute as a string or null if it is not contained.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getAttributeNames ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a list of attribute names.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" class="external-link" title="class or interface in java.lang"><code>Boolean</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBoolean ( String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of a boolean attribute or null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDouble ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of a double precision floating decimal attribute or null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" class="external-link" title="class or interface in java.lang"><code>Float</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFloat ( String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of a single precision floating decimal attribute or null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang"><code>Long</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInt64 ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of a 64-bits integer attribute or null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getString ( String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the value of a string attribute or null if it is not contained or the type doesn't match.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">`DataAttributeValue`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getValue ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the DataAttributeValue or null if it is not contained.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue-valuetype" title="enum class in com.here.sdk.mapview.datasource">`DataAttributeValue.ValueType`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getValueType ( String name)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the value type of an attribute or null if it is not contained.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes an attribute by name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeAll ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes all attributes.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-java-lang-String" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Adds or replaces a string attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-long" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, long value)</span>

    </div>

    <div class="block">

    Adds or replaces a 64-bits integer attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-float" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, float value)</span>

    </div>

    <div class="block">

    Adds or replaces a single precision floating decimal attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-double" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, double value)</span>

    </div>

    <div class="block">

    Adds or replaces a double precision floating decimal attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-boolean" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, boolean value)</span>

    </div>

    <div class="block">

    Adds or replaces a boolean attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-com-here-sdk-core-Color" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span>

    </div>

    <div class="block">

    Adds or replaces a color attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-addOrReplace-java-lang-String-com-here-sdk-mapview-datasource-DataAttributeValue" class="section detail">

    ### addOrReplace

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addOrReplace</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a> value)</span>

    </div>

    <div class="block">

    Adds or replaces an attribute.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    `value` -

    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-remove-java-lang-String" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Removes an attribute by name.

    </div>

    Parameters:  
    `name` -

    Attribute name.

    </div>

  - <div id="sdk-for-android-navigate-removeAll" class="section detail">

    ### removeAll

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeAll</span>()

    </div>

    <div class="block">

    Removes all attributes.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getAttributeNames" class="section detail">

    ### getAttributeNames

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\></span> <span class="element-name">getAttributeNames</span>()

    </div>

    <div class="block">

    Returns a list of attribute names.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getAttributeNames(">`getAttributeNames`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Returns:  
    The list of attribute names.

    </div>

  - <div id="sdk-for-android-navigate-getValueType-java-lang-String" class="section detail">

    ### getValueType

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue-valuetype" title="enum class in com.here.sdk.mapview.datasource">DataAttributeValue.ValueType</a></span> <span class="element-name">getValueType</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the value type of an attribute or null if it is not contained.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getValueType(java.lang.String">`getValueType`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value type or `null` if it is not contained.

    </div>

  - <div id="sdk-for-android-navigate-getAsString-java-lang-String" class="section detail">

    ### getAsString

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of an attribute as a string or null if it is not contained.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getAsString(java.lang.String">`getAsString`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-getString-java-lang-String" class="section detail">

    ### getString

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getString</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a string attribute or null if it is not contained or the type doesn't match.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getString(java.lang.String">`getString`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-getInt64-java-lang-String" class="section detail">

    ### getInt64

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" class="external-link" title="class or interface in java.lang">Long</a></span> <span class="element-name">getInt64</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a 64-bits integer attribute or null if it is not contained or the type doesn't match.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getInt64(java.lang.String">`getInt64`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-getFloat-java-lang-String" class="section detail">

    ### getFloat

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Float.html" class="external-link" title="class or interface in java.lang">Float</a></span> <span class="element-name">getFloat</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a single precision floating decimal attribute or null if it is not contained or the type doesn't match.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getFloat(java.lang.String">`getFloat`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-getDouble-java-lang-String" class="section detail">

    ### getDouble

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getDouble</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a double precision floating decimal attribute or null if it is not contained or the type doesn't match.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getDouble(java.lang.String">`getDouble`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-getBoolean-java-lang-String" class="section detail">

    ### getBoolean

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" class="external-link" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">getBoolean</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the value of a boolean attribute or null if it is not contained or the type doesn't match.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getBoolean(java.lang.String">`getBoolean`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  - <div id="sdk-for-android-navigate-getValue-java-lang-String" class="section detail">

    ### getValue

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributevalue" title="class in com.here.sdk.mapview.datasource">DataAttributeValue</a></span> <span class="element-name">getValue</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Gets the DataAttributeValue or null if it is not contained.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase#getValue(java.lang.String">`getValue`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-dataattributesbase" title="interface in com.here.sdk.mapview.datasource">`DataAttributesBase`</a>

    Parameters:  
    `name` -

    Attribute name.

    Returns:  
    Attribute value.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

