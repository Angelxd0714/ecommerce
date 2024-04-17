<script>
  import { Button, Dropdown, DropdownItem, Checkbox, GradientButton } from 'flowbite-svelte';
  import { ChevronDownOutline } from 'flowbite-svelte-icons';
  export let nombre = "";
</script>

<Button color="alternative" pill>Filtre por: {nombre}</Button>
<Dropdown class="w-44 p-3 space-y-3 text-sm">
  <li>
    <Checkbox>Default checkbox</Checkbox>
  </li>
  <li>
    <Checkbox checked>Checked state</Checkbox>
  </li>
  <li>
    <Checkbox>Default checkbox</Checkbox>
  </li>
</Dropdown>