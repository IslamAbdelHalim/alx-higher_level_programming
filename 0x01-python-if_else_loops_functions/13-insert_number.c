#include "lists.h"

/**
 * insert_node - function that insert node in sorted linked list
 *
 * @head: pointer to head linked lis
 *
 * @number: the number of node
 *
 * Return: the address of new node or null if it faild
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node, *temp;

	current = *head;
	temp = *head;
	/*creating new node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL)
	{
		if (current->n > new_node->n)
		{
			new_node->next = current;

			if (current == *head)
			{
				*head = new_node;
				return (new_node);
			}
			else
			{
				temp->next = new_node;
				return (new_node);
			}
		}
		temp = current;
		current = current->next;
	}
	if (current->next == NULL)
		current->next = new_node;
	return (new_node);
}
