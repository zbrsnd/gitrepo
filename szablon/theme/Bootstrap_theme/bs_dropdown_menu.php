<?php if (!$item->hasChildren) { ?>
    <li class="nav-item <?php echo $item->classes; echo ($item->isCurrent)?' active':''; ?>">
        <a class="nav-link" href="<?php echo htmlspecialchars($item->link); ?>">
            <?php echo htmlspecialchars($item->text); echo ($item->isCurrent)?' <span class="sr-only">(aktualna)</span>':'';?>
        </a>
    </li>

<?php } else {?>

    <li class="nav-item dropdown <?php echo $item->classes; echo ($item->isCurrent)?' active':''; ?>">
        <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
            <?php echo htmlspecialchars($item->text); echo ($item->isCurrent)?' <span class="sr-only">(aktualna)</span>':'';?>
        </a>

        <div class="dropdown-menu">

                <?php
                $pages = return_i18n_pages();
                echo '<a class="dropdown-item" href="'.htmlspecialchars($item->link).'">'.htmlspecialchars($item->text).'</a>';
                foreach (@$pages[$item->slug]['children'] as $child){
                    echo '<a class="dropdown-item" href="'.find_url($child, null).'">'.$pages[$child]['menu'].'</a>';
                }

                ?>

        </div>
    </li>
<?php }?>